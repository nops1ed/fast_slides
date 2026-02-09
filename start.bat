@echo off

REM fast-slides launcher (Windows)

echo [FAST-SLIDES] Initializing...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.9+ first.
    pause
    exit /b 1
)

REM Check Python version
for /f "tokens=2" %%i in ('python --version') do set PYTHON_VERSION=%%i
for /f "tokens=1 delims=." %%i in ("%PYTHON_VERSION%") do set PYTHON_MAJOR=%%i
for /f "tokens=2 delims=." %%i in ("%PYTHON_VERSION%") do set PYTHON_MINOR=%%i

if %PYTHON_MAJOR% lss 3 (
    echo [ERROR] Python version too low. Need Python 3.9+, current version: %PYTHON_VERSION%
    pause
    exit /b 1
)

if %PYTHON_MAJOR% equ 3 if %PYTHON_MINOR% lss 9 (
    echo [ERROR] Python version too low. Need Python 3.9+, current version: %PYTHON_VERSION%
    pause
    exit /b 1
)

REM Check if in project directory
if not exist "fast_slides" (
    echo [ERROR] fast_slides directory not found. Please run this script in the project root.
    pause
    exit /b 1
)

REM Build slides
REM Check if a markdown file is provided as argument
if "%~1" neq "" (    if "%~x1" equ ".md" (
        set "TARGET_FILE=%~1"
        echo [BUILD] Processing %TARGET_FILE%...
        python run.py build "%TARGET_FILE%"
    ) else (
        echo [ERROR] Invalid file type. Please provide a .md file.
        pause
        exit /b 1
    )
) else (
    REM Default to sample_slide.md if no file provided
    set "TARGET_FILE=sample_slide.md"
    echo [BUILD] No markdown file specified, using default: %TARGET_FILE%
    echo [INFO] To build a specific file: %~nx0 your_file.md
    python run.py build "%TARGET_FILE%"
)

REM Check if build succeeded
if %errorlevel% equ 0 (
    echo [SUCCESS] Slides built successfully!
    echo [INFO] Output file: dist/index.html
    echo [INFO] Open this file in your browser to view the slides.
) else (
    echo [ERROR] Build failed. Check your Markdown file.
    echo [INFO] Use command line interface:
    echo [INFO] Example: python run.py build slide.md
)

REM Script end
echo [FAST-SLIDES] Exited.
pause
