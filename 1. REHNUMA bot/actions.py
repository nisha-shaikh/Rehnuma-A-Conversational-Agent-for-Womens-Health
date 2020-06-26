# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

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


# storage.child("glossary.json").download("glossary.json")


class ActionBabyGrowth(Action):
    def __init__(self):
    	growth_data = storage.child("growth_data.json").get_url(None)
    	self.data = pd.read_json(growth_data)
    	self.name()
    	
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
            myimage = storage.child('/baby_growth/week'+duration+'.jpg').get_url(None)
            
            dispatcher.utter_message(image = myimage,
                                     text = mytext)
            return [AllSlotsReset()]


#Accessing glossary.json locally-saved in the same folder
#with open("glossary.json", "r") as read_file:
#            data = json.load(read_file)


class ActionGetGlossary(Action):
    def __init__(self):
    	glossary_data = storage.child("glossary.json").get_url(None)
    	self.data = pd.read_json(glossary_data)
    	self.name()
    	
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
        

        #print ("type", type(meaning))
        
        dispatcher.utter_message(text = meaning)
        
        print(search_word)
        print("meaning",meaning)

        return [SlotSet('word', None)]
        #return []
