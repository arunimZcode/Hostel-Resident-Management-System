@echo off
echo ==========================================
echo      Hostel HMS - Auto Runner
echo ==========================================

:: Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in your PATH.
    echo Please install Python from https://www.python.org/
    pause
    exit /b
)

:: Check if venv exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
) else (
    echo Virtual environment found.
)

:: Activate venv
echo Activating virtual environment...
call venv\Scripts\activate.bat

:: Install dependencies
echo Checking dependencies...
pip install -r requirements.txt >nul 2>&1

:: Run Migrations (Optional but good for safety)
echo Applying database migrations...
python manage.py migrate >nul 2>&1

:: Start Server
echo.
echo Starting Django Server...
echo Opening browser...
start http://127.0.0.1:8000/
python manage.py runserver

pause
