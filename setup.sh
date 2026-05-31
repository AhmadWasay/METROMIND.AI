#!/bin/bash

# MetroMind AI - Setup Script for macOS/Linux

echo ""
echo "========================================"
echo " MetroMind AI - Setup Script"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.9+ from https://www.python.org/"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed or not in PATH"
    echo "Please install Node.js 16+ from https://nodejs.org/"
    exit 1
fi

echo "Python and Node.js are installed!"
echo ""

# Setup Backend
echo "========================================"
echo "Setting up Backend..."
echo "========================================"
cd backend

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing Python packages..."
pip install -r requirements.txt

echo "Backend setup complete!"
cd ..

# Setup Frontend
echo ""
echo "========================================"
echo "Setting up Frontend..."
echo "========================================"
cd frontend

echo "Installing npm packages..."
npm install

echo "Frontend setup complete!"
cd ..

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "To start the application:"
echo ""
echo "1. Terminal 1 - Backend:"
echo "   cd backend"
echo "   source venv/bin/activate"
echo "   uvicorn main:app --reload"
echo ""
echo "2. Terminal 2 - Frontend:"
echo "   cd frontend"
echo "   npm start"
echo ""
echo "Then open your browser to http://localhost:3000"
echo ""