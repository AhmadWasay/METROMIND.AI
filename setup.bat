@echo off
REM MetroMind AI - Setup Script for Windows

echo.
echo ========================================
echo  MetroMind AI - Setup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://www.python.org/
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js 16+ from https://nodejs.org/
    pause
    exit /b 1
)

echo Python and Node.js are installed!
echo.

REM Setup Backend
echo ========================================
echo Setting up Backend...
echo ========================================
cd backend
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing Python packages...
pip install -r requirements.txt

echo Backend setup complete!
cd ..

REM Setup Frontend
echo.
echo ========================================
echo Setting up Frontend...
echo ========================================
cd frontend

echo Installing npm packages...
call npm install

echo Frontend setup complete!
cd ..

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the application:
echo.
echo 1. Terminal 1 - Backend:
echo    cd backend
echo    venv\Scripts\activate
echo    uvicorn main:app --reload
echo.
echo 2. Terminal 2 - Frontend:
echo    cd frontend
echo    npm start
echo.
echo Then open your browser to http://localhost:3000
echo.
pause