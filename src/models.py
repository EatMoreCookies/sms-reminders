from pydantic import BaseModel
from typing import Optional


class Reminder(BaseModel):
    id: Optional[str] = None
    user_id: Optional[str] = None
    message: str
