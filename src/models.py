from pydantic import BaseModel
from typing import Optional


class Reminder(BaseModel):
    user_id: str
    message: str

class User(BaseModel):
    user_id: str
    phone_number: str