# Contact Form Application

A FastAPI-based contact form application with data validation and JSON file storage.

## Features

- ✅ **FastAPI** web framework
- ✅ **Data validation** with custom schemas
- ✅ **JSON file storage** (no database required)
- ✅ **RESTful API** endpoints
- ✅ **Interactive API documentation** (Swagger UI)
- ✅ **Error handling** and logging
- ✅ **Test script** included

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/nevinsebastian/mishapp.git
cd mishapp
```

### 2. Set Up Python Environment

**Option A: Using Python 3.11+ (Recommended)**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Option B: Using Python 3.13 (If you have compatibility issues)**
```bash
# Create virtual environment
python3.13 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Application

```bash
# Start the server
uvicorn appform.app.main:app --reload

# Or with specific host and port
uvicorn appform.app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Access the Application

- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health
- **Root Endpoint**: http://localhost:8000/

## Troubleshooting

### Issue: `uvicorn: command not found`

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Check if uvicorn is installed
pip list | grep uvicorn

# If not installed, install it
pip install uvicorn[standard]

# Or run with python module
python -m uvicorn appform.app.main:app --reload
```

### Issue: `ModuleNotFoundError: No module named 'app'`

**Solution:**
```bash
# Make sure you're in the project root directory
cd /path/to/mishapp

# Run from the correct directory
uvicorn appform.app.main:app --reload
```

### Issue: `Address already in use`

**Solution:**
```bash
# Kill existing processes on port 8000
lsof -ti:8000 | xargs kill -9

# Or use a different port
uvicorn appform.app.main:app --port 8001 --reload
```

### Issue: Python 3.13 Compatibility Issues

**Solution:**
```bash
# Use Python 3.11 or 3.12 instead
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## API Endpoints

### POST `/contact`
Submit a new contact form.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Hello, this is a test message!"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Hello, this is a test message!"
}
```

### GET `/contacts`
Get all contact form submissions.

### GET `/health`
Health check endpoint.

### GET `/`
Root endpoint with basic information.

## Testing the API

### Using the Test Script

```bash
# Run the included test script
python test_api.py
```

### Using curl

```bash
# Test health check
curl http://localhost:8000/health

# Submit a contact form
curl -X POST "http://localhost:8000/contact" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Test User",
       "email": "test@example.com",
       "message": "This is a test message"
     }'

# Get all contacts
curl http://localhost:8000/contacts
```

### Using the HTML Form

Open `contact_form.html` in your browser and submit forms through the web interface.

## Project Structure

```
mishapp/
├── appform/
│   └── app/
│       ├── main.py          # FastAPI application
│       ├── schemas.py       # Data validation schemas
│       ├── database.py      # Database configuration (unused)
│       └── models.py        # Data models (unused)
├── requirements.txt         # Python dependencies
├── test_api.py             # API test script
├── contact_form.html       # HTML form for testing
├── contact_forms.json      # Data storage file (created automatically)
└── README.md               # This file
```

## Dependencies

- `fastapi==0.104.1` - Web framework
- `uvicorn[standard]==0.24.0` - ASGI server
- `python-multipart==0.0.6` - Form data handling
- `requests` - HTTP client for testing

## Data Storage

The application uses JSON file storage (`contact_forms.json`) instead of a traditional database. This makes it easy to set up and run without additional database configuration.

## Development

### Adding New Features

1. Modify the schemas in `appform/app/schemas.py`
2. Update the API endpoints in `appform/app/main.py`
3. Test your changes with `test_api.py`
4. Update this README if needed

### Code Quality

The application includes:
- Input validation
- Error handling
- Logging
- Type hints
- API documentation

## Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Ensure Python 3.11+ is being used
3. Verify all dependencies are installed
4. Check that the virtual environment is activated
5. Make sure you're running from the correct directory

## License

This project is open source and available under the MIT License.