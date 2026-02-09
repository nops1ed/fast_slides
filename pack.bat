@echo off

REM fast-slides packer (Windows)

echo [PACKER] Initializing...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.9+ first.
    pause
    exit /b 1
)

REM Check if in project directory
if not exist "fast_slides" (
    echo [ERROR] fast_slides directory not found. Please run this script in the project root.
    pause
    exit /b 1
)

REM Check if dist directory exists
if not exist "dist" (
    echo [ERROR] dist directory not found. Please build slides first.
    echo [INFO] Run start.bat to build slides.
    pause
    exit /b 1
)

REM Create zip file using Python
set "ZIP_FILE=slides-%date:~0,4%%date:~5,2%%date:~8,2%-%time:~0,2%%time:~3,2%%time:~6,2%.zip"
echo [PACKER] Creating zip file: %ZIP_FILE%

REM Use Python's zipfile module to create the archive
python -c "
import zipfile
import os
import datetime

# Generate timestamp for filename
timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
zip_file = 'slides-' + timestamp + '.zip'
dist_dir = 'dist'

print(f'Creating zip file: {zip_file}')

with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(dist_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, dist_dir)
            zf.write(file_path, arcname)

print(f'Successfully created: {zip_file}')
"

REM Check if zip file exists
if exist "slides-*.zip" (
    echo [SUCCESS] Zip file created successfully!
    echo [INFO] You can now share this zip file.
    echo [INFO] To unpack, simply extract the zip file and open index.html in a browser.
) else (
    echo [ERROR] Failed to create zip file.
)

REM Script end
echo [PACKER] Exited.
pause
