# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#For resetting slots
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset


import pyrebase
import pandas as pd
import json

config = {
    "apiKey": "AIzaSyC0H04FMCRI4eDEbhKoElJ9HF9DHjMdfy8",
    "authDomain": "chatbot-6cdf9.firebaseapp.com",
    "databaseURL": "https://chatbot-6cdf9.firebaseio.com",
    "projectId": "chatbot-6cdf9",
    "storageBucket": "chatbot-6cdf9.appspot.com",
    "messagingSenderId": "653349648297",
    "appId": "1:653349648297:web:4b1a9dfd185500cd1f36b8",
    "measurementId": "G-7SE1G5MLT8"}

firebase= pyrebase.initialize_app(config)
storage = firebase.storage()




class ActionBabyGrowth(Action):
    def __init__(self):
    	# growth_data = storage.child("growth_data.json").get_url(None)
    	# self.data = pd.read_json(growth_data)
        self.data = pd.read_json("./data/growth_data.json")
    	
    def name(self) -> Text:
        return "action_baby_growth"

    def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        duration = tracker.get_slot('pregnancy_duration')
        if duration == None:
            dispatcher.utter_message(text = "I need to know a valid duration of your pregnancy to tell you how big your baby is now. Please tell me in weeks how far along you are in your pregnancy.")
        else:
            mytext = "I see you are {} weeks pregnant. ".format(duration)
            mytext+=self.data[self.data.week==int(duration)].description.item()
            mytext+= "\n" + "Copywrites for the following image belong to babycenter.com"
            myimage = storage.child('/baby_growth/week'+duration+'.jpg').get_url(None)
            # myimage = "./data/images/"+duration+".jpg"
            
            dispatcher.utter_message(image = myimage,
                                     text = mytext)
            return [AllSlotsReset()]



class ActionGetGlossary(Action):
    def __init__(self):
    	# glossary_data = storage.child("glossary.json").get_url(None)
    	# self.data = pd.read_json(glossary_data)
        self.data = pd.read_json("./data/glossary.json")
    	
    def name(self) -> Text:
        return "action_get_glossary"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:    
        
        search_word = tracker.get_slot('word')
        pd.options.display.max_colwidth = 10000
        
        if (search_word is None):
            meaning="I am sorry I don't know what that is, please try something else."
        else:
            meaning= self.data[self.data.Word.str.upper()==search_word.upper()].Meaning
            meaning=meaning.to_string(index=False)     
        

        
        dispatcher.utter_message(text = meaning)
        
        print(search_word)
        print("meaning",meaning)

        return [SlotSet('word', None)]

class ActionDefaultAskAffirmation(Action):
   """Asks for an affirmation of the intent if NLU threshold is not met."""

   def __init__(self):
       self.intent_mappings = pd.read_csv('./data/intent_mappings.csv')    

   def name(self):
       return "action_default_ask_affirmation"


   def run(self, dispatcher, tracker, domain):
       # get the most likely intent
       last_intent_name = tracker.latest_message['intent']['name']
       print(last_intent_name)

       # get the prompt for the intent
       intent_prompt = self.intent_mappings[self.intent_mappings.intent_name==last_intent_name]['mapping'].item()
       print(intent_prompt)

       message = intent_prompt
       buttons = [{'title': 'Yes',
                   'payload': '/{}'.format(last_intent_name)},
                  {'title': 'No',
                   'payload': '/out_of_scope'}]
       dispatcher.utter_message(text = message, buttons=buttons)

       return []

class ActionFeedback(Action):
   """Asks for feedback from the user"""   

   def name(self):
       return "action_feedback"


   def run(self, dispatcher, tracker, domain):

       message = "On a scale of 1-5, how satisfied are you with our bot's conversation?"
       payload = '/feedback_done'
       buttons = [{'title': '1',
                   'payload': payload},
                  {'title': '2',
                   'payload': payload},
                   {'title': '3',
                   'payload': payload},
                   {'title': '4',
                   'payload': payload},
                   {'title': '5',
                   'payload': payload}]

       dispatcher.utter_button_message(message, buttons=buttons)

       return []