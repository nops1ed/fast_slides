import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import subprocess
from fast_slides.converter import converter


class SlideGUI:
    """Slide conversion GUI"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("fast-slides Converter")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        # Set window icon (if available)
        # self.root.iconbitmap("path/to/icon.ico")
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create title
        self.title_label = ttk.Label(
            self.main_frame, 
            text="fast-slides Slide Generator", 
            font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=(0, 20))
        
        # Create drop area
        self.drop_frame = ttk.LabelFrame(
            self.main_frame, 
            text="Drop Markdown file here", 
            padding="20"
        )
        self.drop_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Drop hint
        self.drop_label = ttk.Label(
            self.drop_frame, 
            text="Or click the button below to select file", 
            font=("Arial", 12)
        )
        self.drop_label.pack(expand=True)
        
        # File path display
        self.file_path_var = tk.StringVar()
        self.file_path_entry = ttk.Entry(
            self.main_frame, 
            textvariable=self.file_path_var, 
            state="readonly"
        )
        self.file_path_entry.pack(fill=tk.X, pady=(0, 10))
        
        # Button frame
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Select file button
        self.select_button = ttk.Button(
            self.button_frame, 
            text="Select File", 
            command=self.select_file
        )
        self.select_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Convert button
        self.convert_button = ttk.Button(
            self.button_frame, 
            text="Convert", 
            command=self.convert_file,
            style="Accent.TButton"
        )
        self.convert_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Preview button
        self.preview_button = ttk.Button(
            self.button_frame, 
            text="Preview", 
            command=self.preview_slide,
            state=tk.DISABLED
        )
        self.preview_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Pack button
        self.pack_button = ttk.Button(
            self.button_frame, 
            text="Pack", 
            command=self.pack_slide,
            state=tk.DISABLED
        )
        self.pack_button.pack(side=tk.LEFT)
        
        # Status label
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(
            self.main_frame, 
            textvariable=self.status_var,
            font=("Arial", 10)
        )
        self.status_label.pack(anchor=tk.W)
        
        # Output path label
        self.output_var = tk.StringVar(value="")
        self.output_label = ttk.Label(
            self.main_frame, 
            textvariable=self.output_var,
            font=("Arial", 10),
            wraplength=560
        )
        self.output_label.pack(anchor=tk.W, pady=(5, 0))
        
        # Setup drag & drop
        self.setup_drag_drop()
        
        # Setup styles
        self.setup_styles()
    
    def setup_styles(self):
        """Setup styles"""
        style = ttk.Style()
        style.configure(
            "Accent.TButton", 
            foreground="white",
            background="#4CAF50"
        )
        style.map(
            "Accent.TButton",
            background=[("active", "#45a049")]
        )
    
    def setup_drag_drop(self):
        """Setup drag & drop functionality"""
        # Bind drag events
        self.drop_frame.bind("<DragEnter>", self.on_drag_enter)
        self.drop_frame.bind("<DragLeave>", self.on_drag_leave)
        self.drop_frame.bind("<Drop>", self.on_drop)
        
        # Allow drop
        self.drop_frame.drop_target_register(tk.DND_FILES)
    
    def on_drag_enter(self, event):
        """Drag enter event"""
        self.drop_frame.config(style="Accent.TLabelFrame")
        return event.action
    
    def on_drag_leave(self, event):
        """Drag leave event"""
        self.drop_frame.config(style="TLabelFrame")
    
    def on_drop(self, event):
        """Drop event"""
        self.drop_frame.config(style="TLabelFrame")
        
        # Get dropped file path
        file_path = event.data
        # Process path format (remove braces)
        if file_path.startswith("{") and file_path.endswith("}"):
            file_path = file_path[1:-1]
        
        # Check if file is Markdown
        if file_path.endswith(".md"):
            self.file_path_var.set(file_path)
            self.status_var.set("File selected")
            self.preview_button.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Please select Markdown file (.md)")
    
    def select_file(self):
        """Select file"""
        file_path = filedialog.askopenfilename(
            title="Select Markdown File",
            filetypes=[("Markdown Files", "*.md"), ("All Files", "*.*")]
        )
        
        if file_path:
            self.file_path_var.set(file_path)
            self.status_var.set("File selected")
            self.preview_button.config(state=tk.NORMAL)
    
    def convert_file(self):
        """Convert file"""
        file_path = self.file_path_var.get()
        
        if not file_path:
            messagebox.showwarning("Warning", "Please select a Markdown file first")
            return
        
        try:
            self.status_var.set("Converting...")
            self.root.update()
            
            # Execute conversion
            converter(file_path)
            
            # Calculate output path
            output_dir = os.path.join(os.path.dirname(file_path), "dist")
            output_file = os.path.join(output_dir, "index.html")
            
            self.status_var.set("Conversion complete")
            self.output_var.set(f"Output: {output_file}")
            
            # Update button states
            self.preview_button.config(state=tk.NORMAL)
            self.pack_button.config(state=tk.NORMAL)
            
            # Auto preview
            self.preview_slide()
            
        except Exception as e:
            self.status_var.set("Conversion failed")
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
    
    def pack_slide(self):
        """Pack slides"""
        file_path = self.file_path_var.get()
        
        if not file_path:
            messagebox.showwarning("Warning", "Please select a Markdown file first")
            return
        
        # Calculate output path
        output_dir = os.path.join(os.path.dirname(file_path), "dist")
        output_file = os.path.join(output_dir, "index.html")
        
        # Check if file exists
        if not os.path.exists(output_file):
            messagebox.showwarning("Warning", "Please convert the file first")
            return
        
        try:
            self.status_var.set("Packing...")
            self.root.update()
            
            # Create ZIP file
            import shutil
            zip_path = os.path.join(os.path.dirname(file_path), "slides")
            shutil.make_archive(zip_path, "zip", output_dir)
            zip_file = f"{zip_path}.zip"
            
            self.status_var.set("Packing complete")
            self.output_var.set(f"Packed: {zip_file}")
            messagebox.showinfo("Success", f"Slides packed successfully!\nPath: {zip_file}")
            
        except Exception as e:
            self.status_var.set("Packing failed")
            messagebox.showerror("Error", f"Packing failed: {str(e)}")
    
    def preview_slide(self):
        """Preview slides"""
        file_path = self.file_path_var.get()
        
        if not file_path:
            messagebox.showwarning("Warning", "Please select a Markdown file first")
            return
        
        # Calculate output path
        output_dir = os.path.join(os.path.dirname(file_path), "dist")
        output_file = os.path.join(output_dir, "index.html")
        
        # Check if file exists
        if not os.path.exists(output_file):
            messagebox.showwarning("Warning", "Please convert the file first")
            return
        
        try:
            # Open with system default app
            if os.name == "nt":  # Windows
                os.startfile(output_file)
            else:  # macOS/Linux
                subprocess.run(["open", output_file] if os.name == "posix" else ["xdg-open", output_file])
            
            self.status_var.set("Previewing")
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open preview: {str(e)}")


def main():
    """Main function"""
    try:
        root = tk.Tk()
        app = SlideGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"[GUI] Failed to start: {str(e)}")
        print("Use command line interface instead.")
        print("Example: python3 run.py slide.md")


if __name__ == "__main__":
    main()
