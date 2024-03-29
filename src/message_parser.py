from database_client import DatabaseClient
from models import Reminder, User
import uuid

class MessageParser:
    def __init__(self):
        self.__db_client = DatabaseClient()
        
        self.__fetch_reminders_key: str = 'fetch'
        self.__add_reminder_key: str = 'add'
        self.__remove_reminder_key = 'remove'

    def add_reminder(self, user_id: str, reminder_message: str):
        reminder = Reminder(user_id=user_id, message=reminder_message)
        self.__db_client.add_new_reminder(reminder)
        
        return "Reminder Added - {}".format(reminder_message)
    
    def get_reminders(self, user_id: str):
        reminders: list = []
        reminders_cursor = self.__db_client.get_all_reminders_for_user(user_id)
        
        for r in reminders_cursor:
            reminders.append(r['message'])
        
        return "All Reminders:\n-{}".format("\n-".join(reminders))

    def get_current_user(self, from_phone_number):
        user = self.__db_client.get_user_by_phone_number(from_phone_number)
        is_new = False

        if user is None:
            user = User(user_id=str(uuid.uuid1()), phone_number=from_phone_number)
            self.__db_client.update_user(user)
            is_new = True

        return (user, is_new)

    def determine_response_body_from_message(self, from_phone_number, message: str):
        (current_user, is_new) = self.get_current_user(from_phone_number)

        response: str = ''

        if is_new:
            response += 'Welcome New User {}.'.format(current_user.phone_number)

        if message.lower().strip().startswith(self.__fetch_reminders_key):
            response += self.get_reminders(current_user.user_id)

        elif message.lower().strip().startswith(self.__add_reminder_key):
            response += self.add_reminder(current_user.user_id, message.lower().removeprefix(self.__add_reminder_key)) 

        else:
            response = "Hmmm sorry we are not sure what you mean :/ Please try again :)"

        return response