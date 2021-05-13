# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
# now = datetime.now()
#         hrs= (int(now.strftime("%H"))+0)%24
#         min= (int(now.strftime("%M"))+00)%60
#  final_time=hrs+offset
#         time=str(final_time)+":"+str(min)
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from datetime import datetime


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_relative"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         now = datetime.now()
#         hrs= (int(now.strftime("%H"))+7)%24
#         min= (int(now.strftime("%M"))+30)%60
#         offset=int(tracker.get_slot("number_of_hours"))
#         final_time=hrs+offset
#         time=str(final_time)+":"+str(min)
#         print("Sure, I have scheduled a cleaning at "+time)
#         dispatcher.utter_message(text="Sure, I have scheduled a cleaning at "+time)

#         return []

class ActionTime(Action):
    
    def name(self) -> Text:
        return "action_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        offset=str(tracker.get_slot("time"))
       
        print("Sure, I have scheduled a booking at "+offset)
        dispatcher.utter_message(text="Sure, I have scheduled a booking at "+offset)

        return []

class ActionOpen(Action):
    
    def name(self) -> Text:
        return "action_open_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="The restaurant opens at 7pm and closes at 10pm.")

        return []    


class ActionDays(Action):
    
    def name(self) -> Text:
        return "action_days"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="The restaurant is open each and every day.")

        return []


class ActionCancel(Action):
    
    def name(self) -> Text:
        return "action_cancel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="To cancel a reservation, simply call us at +91 9876543210 and cancel your reservation")

        return []


class ActionSpecial(Action):
    
    def name(self) -> Text:
        return "action_special"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Our chef is a master of the Italian cuisine. Our core speciality is our pasta, which is renowned throughout the city.")

        return []
