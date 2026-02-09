#!/bin/bash

# fast-slides launcher (macOS/Linux)

echo "[FAST-SLIDES] Initializing..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 not found. Please install Python 3.9+ first."
    read -p "Press Enter to exit..."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1)
echo "[INFO] Python version: $PYTHON_VERSION"

# Skip strict version check
# echo "[INFO] Skipping version check..."

# Check if in project directory
if [ ! -d "fast_slides" ]; then
    echo "[ERROR] fast_slides directory not found. Please run this script in the project root."
    read -p "Press Enter to exit..."
    exit 1
fi

# Build slides
# Check if a markdown file is provided as argument
if [ $# -eq 1 ] && [[ "$1" == *.md ]]; then
    TARGET_FILE="$1"
    echo "[BUILD] Processing $TARGET_FILE..."
    python3 run.py build "$TARGET_FILE"
else
    # Default to sample_slide.md if no file provided
    TARGET_FILE="sample_slide.md"
    echo "[BUILD] No markdown file specified, using default: $TARGET_FILE"
    echo "[INFO] To build a specific file: $0 your_file.md"
    python3 run.py build "$TARGET_FILE"
fi

# Check if build succeeded
if [ $? -eq 0 ]; then
    echo "[SUCCESS] Slides built successfully!"
    echo "[INFO] Output file: dist/index.html"
    echo "[INFO] Open this file in your browser to view the slides."
else
    echo "[ERROR] Build failed. Check your Markdown file."
    echo "[INFO] Use command line interface:"
    echo "[INFO] Example: python3 run.py build slide.md"
fi

# Script end
echo "[FAST-SLIDES] Exited."
read -p "Press Enter to exit..."
