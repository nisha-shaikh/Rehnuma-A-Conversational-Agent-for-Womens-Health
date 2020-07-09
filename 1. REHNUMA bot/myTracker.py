import contextlib
import itertools
import json
import logging
import os
import pickle
import typing
from datetime import datetime, timezone

# noinspection PyPep8Naming
from time import sleep
from typing import Callable, Dict, Iterable, Iterator, List, Optional, Text, Union

from boto3.dynamodb.conditions import Key
from rasa.core import utils
from rasa.core.actions.action import ACTION_LISTEN_NAME
from rasa.core.brokers.broker import EventBroker
from rasa.core.conversation import Dialogue
from rasa.core.domain import Domain
from rasa.core.events import SessionStarted
from rasa.core.trackers import ActionExecuted, DialogueStateTracker, EventVerbosity
from rasa.utils.common import class_from_module_path, raise_warning, arguments_of
from rasa.utils.endpoints import EndpointConfig
from rasa.core.tracker_store import TrackerStore
from rasa.core.channels.socketio import SocketIOInput

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

logger = logging.getLogger(__name__)

class MyTrackerStore(TrackerStore):
    """
    Stores conversation history in Firebase NoSQL

    Property methods:
        conversations: returns the current conversation
    """

    def __init__(
        self,
        domain: Domain,
        url: Optional[Text] = None,
        collection: Optional[Text] = "test",
        event_broker: Optional[EventBroker] = None
    ):
        self.cred = credentials.Certificate(
            "chatbot-6cdf9-firebase-adminsdk-y4mh0-74f3365b45.json")
        firebase_admin.initialize_app(self.cred)

        self.db = firestore.client()
        # self.collection = collection
        super().__init__(domain, event_broker)

        self.chat = self.db.collection('test-chat')
        self.messages = self.db.collection('test-message')

        self.button_click = False
        self.button_appear = False

        # self._ensure_indices()

    # @property
    # def conversations(self):
    #     """Returns the current conversation"""
    #     # return self.db[self.collection]
    #     # self.db.collection('test').add({'here': 2})
    #     return self.db.collection('test')

    # def _ensure_indices(self):
    #     """Create an index on the sender_id"""
    #     self.conversations.create_index("sender_id")

    @staticmethod
    def _current_tracker_state_without_events(tracker: DialogueStateTracker) -> Dict:
        # get current tracker state and remove `events` key from state
        # since events are pushed separately in the `update_one()` operation
        state = tracker.current_state(EventVerbosity.ALL)
        state.pop("events", None)

        return state

    def save(self, tracker, timeout=None):
        """Saves the current conversation state"""
        if self.event_broker:
            self.stream_events(tracker)

        additional_events = self._additional_events(tracker)

        try:
            # if next(self.conversations.where("senderID", '==', tracker.sender_id).limit(1).stream(), None) is None:
            #     # if document doesn't exist, create one
            #     doc_id = self.conversations.document().id
            #     self.conversations.document(doc_id).set(
            #         {"senderID": tracker.sender_id}
            #     )
            # else:
            #     doc_id = next(self.conversations.where(
            #         "senderID", '==', tracker.sender_id).limit(1).stream()).id

            if next(self.chat.where("senderID", '==', tracker.sender_id).limit(1).stream(), None) is None:
                # if document doesn't exist, create one
                visitor_number = 'Visitor {}'.format(
                    len(list(self.chat.stream())) + 1)
                # chat_doc_id = self.chat.document().id
                self.chat.document(visitor_number).set(
                    {"senderID": tracker.sender_id}
                )
            else:
                visitor_number = next(self.chat.where(
                    "senderID", '==', tracker.sender_id).limit(1).stream()).id

            current_state = self._current_tracker_state_without_events(tracker)

            # self.conversations.document(doc_id).set(
            #     current_state
            # )

            chat_doc = self.chat.document(visitor_number).get().to_dict()
            events = [e.as_dict() for e in additional_events]

            response = {'ResponseName': None, 'ResponseText': None}
            time = None
            bye = False

            for e in events:
                if e['event'] == 'session_started':
                    time = datetime.fromtimestamp(e['timestamp'])
                    if 'StartTime' not in chat_doc:
                        # add StartTime of only 1st message
                        self.chat.document(visitor_number).set(
                            {'StartTime': time,
                            'isActive': True,
                            'Flagged': False},
                            merge=True
                        )
                if 'confidence' in e and e['confidence'] == 1 and e['name'] != 'action_listen':
                    # add response name
                    response['ResponseName'] = e['name']
                if e['event'] == 'bot':
                    response['ResponseText'] = e['text']
                    if e['data']['buttons'] is not None:
                        self.button_appear = True
                if e['event'] == 'user' and (e['parse_data']['intent'] == 'goodbye' or e['parse_data']['intent'] == 'feedback_done'):
                    bye = True
                    time = datetime.fromtimestamp(e['timestamp'])
                    self.chat.document(visitor_number).set({
                        'EndTime': time,
                        'isActive': False
                        },
                        merge=True
                    )

            if events:
                logger.debug(events)
                # only add data to database when user sends a message
                new_message = self.messages.document().id          # ID of new text in thread
                if not self.button_click:
                    # if reply is not from button
                    self.messages.document(new_message).set({
                        'chatID': visitor_number,
                        'Time': time,
                        'MessageText': current_state['latest_message']['text'],
                        'Intent': current_state['latest_message']['intent']['name'],
                        'Response': response,
                        'Flagged': False
                    })
                    if self.button_appear:
                        self.button_click = True
                        self.button_appear = False
                else:
                    self.button_click = False
                    e = [e for e in events if e['event'] == 'user']
                    if e[0]['text'] == '/out_of_scope':
                        # if user chose the No button for default_ask_affirmation
                        self.messages.document(new_message).set({
                            'chatID': visitor_number,
                            'Time': time,
                            'MessageText': 'No',
                            'Intent': e[0]['parse_data']['intent']['name'],
                            'Response': response,
                            'Flagged': True
                        })
                        self.chat.document(visitor_number).set({
                            'Flagged': True
                            },
                            merge=True
                        )
                    elif e[0]['text'] == '/affirm':
                        # if user chose the Yes button for feedback
                        self.messages.document(new_message).set({
                            'chatID': visitor_number,
                            'Time': time,
                            'MessageText': 'Yes',
                            'Intent': e[0]['parse_data']['intent']['name'],
                            'Response': response,
                            'Flagged': False
                        })
                    elif e[0]['text'] == '/deny':
                        # if user chose the No button for feedback
                        self.messages.document(new_message).set({
                            'chatID': visitor_number,
                            'Time': time,
                            'MessageText': 'No',
                            'Intent': e[0]['parse_data']['intent']['name'],
                            'Response': response,
                            'Flagged': False
                        })
                    else:
                        # if user chose the Yes button for default_ask_affirmation
                        self.messages.document(new_message).set({
                            'chatID': visitor_number,
                            'Time': time,
                            'MessageText': 'Yes',
                            'Intent': e[0]['parse_data']['intent']['name'],
                            'Response': response,
                            'Flagged': False
                        })

                # self.conversations.document(doc_id).set({
                #     "events": firestore.firestore.ArrayUnion(events)},
                #     merge=True
                # )

        except Exception as err:
            logger.debug('in save new error 1')
            logger.error(err)
            logger.debug(current_state)

    def _additional_events(self, tracker: DialogueStateTracker) -> Iterator:
        """Return events from the tracker which aren't currently stored.

        Args:
            tracker: Tracker to inspect.

        Returns:
            List of serialised events that aren't currently stored.

        """
        stored = None
        number_events_since_last_session = None

        try:
            # stored = next(self.conversations.where("senderID", '==',
            #                                        tracker.sender_id).limit(1).stream()).to_dict() or {}
            stored = next(self.chat.where("senderID", '==',
                                            tracker.sender_id).limit(1).stream()).to_dict() or {}
            number_events_since_last_session = len(
                self._events_since_last_session_start(stored)
            )
        except Exception as e:
            logger.debug('in additional events')
            logger.error(e)

        return itertools.islice(
            tracker.events, number_events_since_last_session, len(
                tracker.events)
        )

    @staticmethod
    def _events_since_last_session_start(serialised_tracker: Dict) -> List[Dict]:
        """Retrieve events since and including the latest `SessionStart` event.

        Args:
            serialised_tracker: Serialised tracker to inspect.

        Returns:
            List of serialised events since and including the latest `SessionStarted`
            event. Returns all events if no such event is found.

        """

        events = []
        for event in reversed(serialised_tracker.get("events", [])):
            events.append(event)
            if event["event"] == SessionStarted.type_name:
                break

        return list(reversed(events))

    def retrieve(self, sender_id):
        """
        Args:
            sender_id: the message owner ID

        Returns:
            `DialogueStateTracker`
        """

        stored = None

        try:
            # stored = next(self.conversations.where("senderID", '==',
            #                                        sender_id).limit(1).stream()).to_dict()

            stored = next(self.chat.where("senderID", '==',
                                            sender_id).limit(1).stream()).to_dict()

            # look for conversations which have used an `int` sender_id in the past
            # and update them.
            # if stored is None and sender_id.isdigit():

            #     doc_id = next(self.conversations.where(
            #         "senderID", '==', int(sender_id)).limit(1).stream()).id

            #     self.conversations.document(doc_id).update({
            #         "senderID": str(sender_id)
            #     })

            #     stored = self.conversations.document(doc_id).get().to_dict()
        except Exception as e:
            logger.debug('in retrieve')
            logger.error(e)

        if stored is not None:
            events = self._events_since_last_session_start(stored)
            return DialogueStateTracker.from_dict(sender_id, events, self.domain.slots)
        else:
            return None

    def keys(self) -> Iterable[Text]:
        """Returns sender_ids of the Mongo Tracker Store"""
        return [c.to_dict()["senderID"] for c in self.chat.stream()]
