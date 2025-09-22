from typing import Optional
import re
from dataclasses import dataclass


@dataclass
class ContactFormCreate:
    name: str
    email: str
    message: str
    
    def __post_init__(self):
        if not self.name or len(self.name.strip()) == 0:
            raise ValueError("Name is required")
        if len(self.name) > 100:
            raise ValueError("Name must be less than 100 characters")
        
        if not self.email or len(self.email.strip()) == 0:
            raise ValueError("Email is required")
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, self.email):
            raise ValueError('Invalid email format')
        
        if not self.message or len(self.message.strip()) == 0:
            raise ValueError("Message is required")
        if len(self.message) > 1000:
            raise ValueError("Message must be less than 1000 characters")


@dataclass
class ContactFormResponse:
    id: int
    name: str
    email: str
    message: str