from database_client import DatabaseClient
from models import Reminder

class MessageParser:
    def __init__(self):
        self.__db_client = DatabaseClient()
        self.__add_reminder_keys: list = [
            "add reminder",
            "addreminder",
            "ar"
            "add-reminder",
            "add"
        ]

        self.__get_reminder_keys: list = [
            "get reminders",
            "getreminders",
            "gr"
            "get-reminders",
            "get"
        ]

    def add_reminder(self, user_id: str, add_reminder_key: str, message: str):
        reminder_message = message.removeprefix(add_reminder_key)
        reminder = Reminder(user_id=user_id, message=reminder_message)
        self.__db_client.add_new_reminder(reminder)
        return "Reminder Added - {}".format(reminder_message)
    
    def get_reminders(self, user_id: str):
        reminders: list = []
        reminders_cursor = self.__db_client.get_all_reminders_for_user(user_id)
        
        for r in reminders_cursor:
            reminders.append(r['message'])
        
        return "All Reminders:\n-{}".format("\n-".join(reminders))

    def determine_response_body_from_message(self, user_id: str, message: str):
        for k in self.__add_reminder_keys:
            if message.lower().startswith(k):
                return self.add_reminder(user_id, k, message)
        
        for k in self.__get_reminder_keys:
            if message.lower().startswith(k):
                return self.get_reminders(user_id)   
