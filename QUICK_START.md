# 🚀 Quick Start Guide

## For Your Friend - Easy Setup

### Option 1: Automatic Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/nevinsebastian/mishapp.git
cd mishapp

# Run the setup script
chmod +x setup.sh
./setup.sh

# Start the application
source venv/bin/activate
uvicorn appform.app.main:app --reload
```

### Option 2: Manual Setup

```bash
# Clone the repository
git clone https://github.com/nevinsebastian/mishapp.git
cd mishapp

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the application
uvicorn appform.app.main:app --reload
```

## 🌐 Access the Application

Once running, visit:
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health
- **Test Form**: Open `contact_form.html` in your browser

## 🧪 Test the API

```bash
# Run the test script
python test_api.py

# Or test manually with curl
curl http://localhost:8000/health
```

## ❗ Common Issues & Solutions

### "uvicorn: command not found"
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Or run with python module
python -m uvicorn appform.app.main:app --reload
```

### "Address already in use"
```bash
# Kill existing processes
lsof -ti:8000 | xargs kill -9

# Or use different port
uvicorn appform.app.main:app --port 8001 --reload
```

### Python 3.13 issues
```bash
# Use Python 3.11 instead
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📱 What This App Does

- ✅ **Contact Form API** - Submit contact forms via REST API
- ✅ **Data Validation** - Validates name, email, and message fields
- ✅ **JSON Storage** - Stores data in `contact_forms.json`
- ✅ **API Documentation** - Interactive Swagger UI at `/docs`
- ✅ **Health Monitoring** - Health check endpoint
- ✅ **Test Suite** - Included test script

## 🎯 API Endpoints

- `POST /contact` - Submit contact form
- `GET /contacts` - Get all submissions
- `GET /health` - Health check
- `GET /` - Root endpoint

That's it! Your contact form application is ready to use! 🎉
