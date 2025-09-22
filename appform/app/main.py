from fastapi import FastAPI, HTTPException, status, Request
from . import schemas
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import logging
import json
import os
from datetime import datetime

app = FastAPI(title="Contact Form API", version="1.0.0")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContactFormRequest(BaseModel):
    name: str
    email: str
    message: str
    
    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "message": "Hello, this is a test message!"
            }
        }

CONTACTS_FILE = "contact_forms.json"

def load_contacts():
    """Load contacts from JSON file"""
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_contacts(contacts):
    """Save contacts to JSON file"""
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=2)

@app.post("/contact", response_model=schemas.ContactFormResponse)
async def create_contact_form(contact_data: ContactFormRequest):
    """
    Create a new contact form submission
    
    - **name**: Full name (required, 1-100 characters)
    - **email**: Email address (required, valid email format)
    - **message**: Message content (required, 1-1000 characters)
    """
    try:
        form_data = schemas.ContactFormCreate(
            name=contact_data.name,
            email=contact_data.email,
            message=contact_data.message
        )
        
        contacts = load_contacts()
        
        new_id = len(contacts) + 1
        contact_entry = {
            "id": new_id,
            "name": form_data.name,
            "email": form_data.email,
            "message": form_data.message,
            "created_at": datetime.now().isoformat()
        }
        
        contacts.append(contact_entry)
        
        save_contacts(contacts)
        
        logger.info(f"New contact form submitted by {form_data.name} ({form_data.email})")
        
        response_data = schemas.ContactFormResponse(
            id=contact_entry["id"],
            name=contact_entry["name"],
            email=contact_entry["email"],
            message=contact_entry["message"]
        )
        
        return response_data
        
    except ValueError as e:
        logger.warning(f"Validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Error creating contact form: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to submit contact form"
        )


@app.post("/contact-raw")
async def create_contact_form_raw(request: Request):
    """
    Create a new contact form submission (raw JSON endpoint)
    """
    try:
        data = await request.json()
        
        form_data = schemas.ContactFormCreate(
            name=data.get("name", ""),
            email=data.get("email", ""),
            message=data.get("message", "")
        )
        
        contacts = load_contacts()
        
        new_id = len(contacts) + 1
        contact_entry = {
            "id": new_id,
            "name": form_data.name,
            "email": form_data.email,
            "message": form_data.message,
            "created_at": datetime.now().isoformat()
        }
        
        contacts.append(contact_entry)
        
        save_contacts(contacts)
        
        logger.info(f"New contact form submitted by {form_data.name} ({form_data.email})")
        
        response_data = schemas.ContactFormResponse(
            id=contact_entry["id"],
            name=contact_entry["name"],
            email=contact_entry["email"],
            message=contact_entry["message"]
        )
        
        return response_data
        
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid JSON format"
        )
    except ValueError as e:
        logger.warning(f"Validation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Error creating contact form: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to submit contact form"
        )


@app.get("/contacts")
async def get_contacts():
    """
    Get all contact form submissions
    """
    try:
        contacts = load_contacts()
        response_contacts = []
        for contact in contacts:
            response_contacts.append(schemas.ContactFormResponse(
                id=contact["id"],
                name=contact["name"],
                email=contact["email"],
                message=contact["message"]
            ))
        return response_contacts
    except Exception as e:
        logger.error(f"Error fetching contacts: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch contacts"
        )


@app.get("/")
async def root():
    return {"message": "Contact Form API is running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}