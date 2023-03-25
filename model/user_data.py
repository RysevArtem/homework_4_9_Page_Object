from dataclasses import dataclass
from enum import Enum


class Subjects(Enum):
    maths = "Maths"
    chemistry = "Chemistry"
    english = "English"
    biology = "Biology"

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: int
    birth_year: str
    birth_month: str
    birth_day: str
    subject: Subjects
    hobby: str
    upload_filename: str
    current_address: str
    state: str
    city: str
