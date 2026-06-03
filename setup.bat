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

echo Checking for .env file...
if not exist .env (
    echo .env file not found. Creating from .env.example...
    copy .env.example .env
)

echo Installing Python packages...
pip install -r requirements.txt

echo Initializing database and checking configuration...
python setup.py

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
echo    (In Command Prompt)
echo    cd backend ^&^& call venv\Scripts\activate.bat ^&^& python main.py
echo.
echo    (In PowerShell)
echo    cd backend; .\venv\Scripts\Activate.ps1; python main.py
echo.
echo 2. Terminal 2 - Frontend:
echo    cd frontend ^&^& npm start
echo.
pause