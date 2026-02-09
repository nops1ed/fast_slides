import sys
import os
import argparse
import time
import subprocess

# Dependency checker
def check_dependencies():
    """Check if all required dependencies are installed"""
    required_deps = [
        "requests",
        "jinja2",
        "markdown",
        "pyquery",
        "pygments",
        "lxml",
        "yaml",  # pyyaml's import name is yaml
        "click",
        "watchdog",
    ]
    
    missing = []
    
    for dep in required_deps:
        try:
            __import__(dep)
        except ImportError:
            missing.append(dep)
    
    if missing:
        print("[ERROR] Missing required dependencies:")
        for dep in missing:
            print(f"  - {dep}")
        print("[INFO] Install with:")
        print(f"  pip3 install {' '.join(missing)}")
        sys.exit(1)

# Run dependency check
check_dependencies()

# Add current dir to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fast_slides.converter import converter
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class SlideEventHandler(FileSystemEventHandler):
    """Slide file event handler"""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
    
    def on_modified(self, event):
        """File modified event"""
        if event.src_path == self.filepath:
            print(f"[WATCHER] {self.filepath} modified, recompiling...")
            try:
                converter(self.filepath)
                print("[WATCHER] Compilation successful!")
            except Exception as e:
                print(f"[WATCHER] Compilation error: {e}")


def init_command():
    """Initialize new slide project"""
    print("[INIT] Bootstrapping new slide project...")
    # Create default markdown file
    default_content = """# Slide Title

## Introduction

--

This is a fragment

---

## Second Slide

Content of second slide
"""
    with open("slide.md", "w", encoding="utf-8") as f:
        f.write(default_content)
    print("[INIT] Default slide.md created")


def build_command(filepath):
    """Build slides from markdown"""
    print(f"[BUILD] Processing {filepath}...")
    try:
        converter(filepath)
        output_dir = os.path.join(os.path.dirname(filepath), "dist")
        output_file = os.path.join(output_dir, "index.html")
        print(f"[BUILD] Success! Output: {output_file}")
    except Exception as e:
        print(f"[BUILD] Error: {e}")


def start_command(filepath, watch, serve):
    """Start slide project with optional watch and serve"""
    # Initial build
    print(f"[START] Initializing slides from {filepath}...")
    try:
        converter(filepath)
        output_dir = os.path.join(os.path.dirname(filepath), "dist")
        output_file = os.path.join(output_dir, "index.html")
        print(f"[START] Build successful! Output: {output_file}")
        
        # Open browser if requested
        if serve:
            print("[START] Launching browser...")
            subprocess.run(["open", output_file])  # Use system default app
        
        # Watch for changes if requested
        if watch:
            print(f"[START] Watching {filepath} for changes...")
            event_handler = SlideEventHandler(filepath)
            observer = Observer()
            observer.schedule(event_handler, os.path.dirname(filepath), recursive=False)
            observer.start()
            
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                observer.stop()
                observer.join()
                print("[START] Watch stopped")
                
    except Exception as e:
        print(f"[START] Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="fast-slides: A fast and elegant slide generator from Markdown")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Build command
    build_parser = subparsers.add_parser("build", help="Build slides from Markdown file")
    build_parser.add_argument("filepath", type=str, help="Path to Markdown file")
    
    # Init command
    init_parser = subparsers.add_parser("init", help="Initialize a new slide project")
    
    # Start command
    start_parser = subparsers.add_parser("start", help="Start slide project with optional watch and serve")
    start_parser.add_argument("filepath", type=str, help="Path to Markdown file")
    start_parser.add_argument("--watch", "-w", action="store_true", help="Watch for file changes and recompile")
    start_parser.add_argument("--serve", "-s", action="store_true", help="Serve slides and open in browser")
    
    # Parse args
    args = parser.parse_args()
    
    # Execute command
    if args.command == "build":
        build_command(args.filepath)
    elif args.command == "init":
        init_command()
    elif args.command == "start":
        start_command(args.filepath, args.watch, args.serve)
    else:
        # Legacy usage support
        if len(sys.argv) == 2:
            build_command(sys.argv[1])
        else:
            parser.print_help()
            sys.exit(1)
