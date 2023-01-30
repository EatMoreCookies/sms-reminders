from twilio_client import TwilioClient
from database_client import DatabaseClient
from models import Reminder
import uuid

twilioClient: TwilioClient = TwilioClient()

# twilioClient.send_message("Hello There Sir!")

#print("Sent!")

client = DatabaseClient()

current_user_id: str = '07d5d47a-a041-11ed-84b6-c8348e4bbf3d'

# reminder = Reminder(message='Do the dishes', user_id=current_user_id)

# client.add_new_reminder(reminder)

# reminder = Reminder(message='Rake the leaves', user_id=current_user_id)

# client.add_new_reminder(reminder)

# reminder = Reminder(message='Mow the lawns', user_id=current_user_id)

# client.add_new_reminder(reminder)

remindersCursor = client.get_all_reminders_for_user(current_user_id)

for r in remindersCursor:
    twilioClient.send_message(r['message'])
    