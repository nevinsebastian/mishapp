#!/usr/bin/env python3
"""
Test script for the Contact Form API
"""

import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_health():
    """Test the health endpoint"""
    print("Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_contact_submission():
    """Test contact form submission"""
    print("Testing contact form submission...")
    
    test_data = {
        "name": "Test User",
        "email": "test@example.com",
        "message": "This is a test message from the Python script!"
    }
    
    response = requests.post(
        f"{BASE_URL}/contact",
        headers={"Content-Type": "application/json"},
        json=test_data
    )
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_get_contacts():
    """Test getting all contacts"""
    print("Testing get all contacts...")
    response = requests.get(f"{BASE_URL}/contacts")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_validation():
    """Test validation with invalid data"""
    print("Testing validation with invalid data...")
    
    invalid_data = {
        "name": "Test User",
        "email": "invalid-email",
        "message": "This should fail validation"
    }
    
    response = requests.post(
        f"{BASE_URL}/contact",
        headers={"Content-Type": "application/json"},
        json=invalid_data
    )
    
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

if __name__ == "__main__":
    print("=== Contact Form API Test ===")
    print()
    
    try:
        test_health()
        test_contact_submission()
        test_get_contacts()
        test_validation()
        
        print("All tests completed!")
        
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"Error: {e}")
