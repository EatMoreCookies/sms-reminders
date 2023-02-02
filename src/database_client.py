from pymongo import MongoClient
import os
from models import Reminder, User

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
        reminder_collection.insert_one(reminder.__dict__)
    
    def get_all_reminders_for_user(self, user_id: str):
        reminder_collection = self.__client.CoreDatabase.Reminders
        return reminder_collection.find({"user_id": user_id})
    
    def update_user(self, user: User):
        user_collection = self.__client.CoreDatabase.Users
        user_collection.insert_one(user.__dict__)
    
    def get_user_by_phone_number(self, phone_number: str):
        user_collection = self.__client.CoreDatabase.Users
        user_json = user_collection.find_one({"phone_number": phone_number})

        if user_json is None:
            return None

        return User(user_id=user_json['user_id'], phone_number=user_json['phone_number'])


