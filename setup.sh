#!/bin/bash

# Contact Form Application Setup Script
# This script will set up the environment and install dependencies

echo "🚀 Setting up Contact Form Application..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11+ first."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Python version: $PYTHON_VERSION"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Check if uvicorn is installed
if command -v uvicorn &> /dev/null; then
    echo "✅ uvicorn is installed and ready"
else
    echo "❌ uvicorn installation failed"
    exit 1
fi

echo ""
echo "🎉 Setup complete! You can now run the application with:"
echo ""
echo "   source venv/bin/activate"
echo "   uvicorn appform.app.main:app --reload"
echo ""
echo "Then visit: http://localhost:8000/docs"
echo ""
