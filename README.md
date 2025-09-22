# Contact Form Application

A FastAPI-based contact form application with proper data validation and JSON file storage.

## Features

- ✅ Contact form with name, email, and message fields
- ✅ Data validation using custom validation with regex email validation
- ✅ JSON file storage (no database setup required)
- ✅ Proper error handling and logging
- ✅ RESTful API endpoints
- ✅ HTML form for testing
- ✅ Interactive API documentation
- ✅ Timestamps for each submission

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   uvicorn appform.app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

3. **Test the form:**
   - Open `contact_form.html` in your browser
   - Or use the API directly at `http://localhost:8000/docs`
   - Run the test script: `python test_api.py`

## API Endpoints

- `POST /contact` - Submit a contact form (with proper schema documentation)
- `POST /contact-raw` - Submit a contact form (raw JSON endpoint)
- `GET /contacts` - Get all contact submissions
- `GET /` - Health check
- `GET /health` - Health status

## Data Validation

The application includes comprehensive data validation:

- **Name**: Required, 1-100 characters
- **Email**: Required, valid email format using regex validation
- **Message**: Required, 1-1000 characters

## Data Storage

Contact forms are stored in `contact_forms.json` with the following structure:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Hello, this is a test message!",
    "created_at": "2025-01-22T12:43:39.123456"
  }
]
```

## Example Usage

### Submit a contact form:
```bash
curl -X POST "http://localhost:8000/contact" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "John Doe",
       "email": "john@example.com",
       "message": "Hello, this is a test message!"
     }'
```

### Get all contacts:
```bash
curl -X GET "http://localhost:8000/contacts"
```

### Using the Interactive API Documentation:
1. Go to `http://localhost:8000/docs`
2. Click on `POST /contact`
3. Click "Try it out"
4. Fill in the example data in the request body
5. Click "Execute"

## Testing

Run the included test script to verify everything works:
```bash
python test_api.py
```

This will test:
- Health endpoint
- Contact form submission
- Getting all contacts
- Validation with invalid data

## Best Practices Implemented

1. **Data Validation**: Custom validation with proper error messages
2. **Error Handling**: Comprehensive error handling with proper HTTP status codes
3. **Logging**: Structured logging for debugging and monitoring
4. **API Design**: RESTful endpoints with proper response models
5. **Security**: Input validation and sanitization
6. **Documentation**: Clear API documentation with FastAPI's automatic docs
7. **Testing**: Included test script for verification
8. **Flexibility**: Both structured and raw JSON endpoints for different use cases
