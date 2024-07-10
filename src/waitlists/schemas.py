from datetime import datetime
from ninja import Schema
from pydantic import EmailStr

class WaitlistEntryListSchema(Schema):
    # List -> Data
    # WaitlistEntryIn
    id: int
    email: EmailStr

class WaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistEntryIn
    email: EmailStr

class WaitlistEntryDetailSchema(Schema):
    # Get -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime