from pymongo import MongoClient
import os
from models import Reminder

class DatabaseClient:
    def __init__(self):
        self.__client: MongoClient = MongoClient(self.create_connection_string())
    
    def create_connection_string(self):
        connection_string: str = "mongodb+srv://{username}:{password}@cluster0.p1yxhqn.mongodb.net/?retryWrites=true&w=majority"
        connection_string = connection_string.format(username=os.environ['SMS_REMINDERS_DB_USERNAME'], password=os.environ['SMS_REMINDERS_DB_PASSWORD'])
        return connection_string
    
    def test_connection(self):
        return self.__client != None

    def add_new_reminder(self, reminder: Reminder):
        reminder_collection = self.__client.CoreDatabase.Reminders
        reminder_collection.insert_one({"user_id": reminder.user_id, "message": reminder.message})
    
    def get_all_reminders_for_user(self, user_id: str):
        reminder_collection = self.__client.CoreDatabase.Reminders
        return reminder_collection.find({"user_id": user_id})

