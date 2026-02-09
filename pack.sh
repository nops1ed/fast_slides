#!/bin/bash

# fast-slides packer (macOS/Linux)

echo "[PACKER] Initializing..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 not found. Please install Python 3.9+ first."
    read -p "Press Enter to exit..."
    exit 1
fi

# Check if in project directory
if [ ! -d "fast_slides" ]; then
    echo "[ERROR] fast_slides directory not found. Please run this script in the project root."
    read -p "Press Enter to exit..."
    exit 1
fi

# Check if dist directory exists
if [ ! -d "dist" ]; then
    echo "[ERROR] dist directory not found. Please build slides first."
    echo "[INFO] Run ./start.sh to build slides."
    read -p "Press Enter to exit..."
    exit 1
fi

# Create zip file
ZIP_FILE="slides-$(date +%Y%m%d-%H%M%S).zip"
echo "[PACKER] Creating zip file: $ZIP_FILE"

# Use zip command to create the archive
if command -v zip &> /dev/null; then
    zip -r "$ZIP_FILE" dist/
else
    # Fallback to using Python's zipfile module
    echo "[INFO] zip command not found, using Python fallback..."
    python3 -c "
import zipfile
import os

zip_file = '$ZIP_FILE'
dist_dir = 'dist'

with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(dist_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, dist_dir)
            zf.write(file_path, arcname)

print(f'Created {zip_file}')
"
fi

# Check if zip file was created
if [ -f "$ZIP_FILE" ]; then
    echo "[SUCCESS] Zip file created: $ZIP_FILE"
    echo "[INFO] You can now share this zip file."
    echo "[INFO] To unpack, simply extract the zip file and open index.html in a browser."
else
    echo "[ERROR] Failed to create zip file."
fi

# Script end
echo "[PACKER] Exited."
read -p "Press Enter to exit..."
