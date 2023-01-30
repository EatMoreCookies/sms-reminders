import os
from twilio.rest import Client

class TwilioClient:
    def __init__(self):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.__client = Client(account_sid, auth_token)
        self.__from_number = '+13143508941'
        self.__test_to_number = '+16054843732'

    def send_message(self, message: str):
        message = self.__client.messages.create(
            body=message,
            from_=self.__from_number,
            to=self.__test_to_number
        )