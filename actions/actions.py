# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import AllSlotsReset,Restarted


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Your conversation has been restarted")

        return [AllSlotsReset()]



class loanForm(FormAction):

    def name(self):
        return "loan_form"

    @staticmethod
    def required_slots(tracker):
        return [
        "person_name",
        "email_id",
        "type_loan",
        "phone_number",
        ]


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any], ) -> List[Dict]:
        dispatcher.utter_message(template="utter_submit")
        return []


class ActionCustom(Action):
   def name(self):
      return "action_custom"

   def run(self, dispatcher, tracker, domain):
      # send utter default response to user
      dispatcher.utter_message(template="utter_default")
      # ... other code
      return []


class loanForm2(FormAction):

    def name(self):
        return "loan_form2"

    @staticmethod
    def required_slots(tracker):
        return [
       "housing_status",
       "other_loans",
       "monthly_salary",
        ]


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any], ) -> List[Dict]:
        dispatcher.utter_message(template="utter_submit2")
        return []



class ActionRestarted(Action):
    def name(self):
        return "action_chat_restart"
    def run(self,dispatcher,tracker,domain):
        return[Restarted()]