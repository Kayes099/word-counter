import tkinter as tk
from tkinter import ttk, messagebox
import re

class WordCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Counter")
        self.root.geometry("600x400")
        self.root.configure(bg="#2d2d2d")
        
        # Make the window resizable
        self.root.resizable(True, True)
        
        # Set minimum window size
        self.root.minsize(400, 300)
        
        self.create_widgets()
        self.apply_style()
    
    def create_widgets(self):
        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title label
        self.title_label = ttk.Label(
            self.main_frame, 
            text="Word Counter", 
            font=('Helvetica', 18, 'bold')
        )
        self.title_label.pack(pady=(0, 20))
        
        # Text input label
        self.input_label = ttk.Label(
            self.main_frame, 
            text="Enter your paragraph:", 
            font=('Helvetica', 10)
        )
        self.input_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Text input area
        self.text_input = tk.Text(
            self.main_frame, 
            height=10, 
            wrap=tk.WORD,
            bg="dark grey",
            fg="black",
            insertbackground="black",
            font=('Helvetica', 10),
            padx=10,
            pady=10
        )
        self.text_input.pack(fill=tk.BOTH, expand=True)
        
        # Button frame
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Count button
        self.count_button = ttk.Button(
            self.button_frame,
            text="Count Words",
            command=self.count_words,
            style="Accent.TButton"
        )
        self.count_button.pack(side=tk.LEFT, padx=(0, 10))
        
        
        
        # Result label
        self.result_label = ttk.Label(
            self.main_frame,
            text="",
            font=('Helvetica', 12),
            foreground="yellow"
        )
        self.result_label.pack(pady=(20, 0))
    
    def apply_style(self):
        style = ttk.Style()
        
        # Configure the main style
        style.configure(
            'TFrame', 
            background="black"
        )
        
        style.configure(
            'TLabel', 
            background="black", 
            foreground="white"
        )
        
        style.configure(
            'TButton', 
            font=('Helvetica', 10),
            padding=6,
            background="#424242",
            foreground="black"
        )
        
        # Accent button style (for Count and Next buttons)
        style.configure(
            'Accent.TButton', 
            font=('Helvetica', 12, 'bold'),
            padding=10,
            background="#1976D2",
            foreground="black",
            
        )
        
        style.map(
            'Accent.TButton',
            background=[('active', '#1565C0'), ('pressed', '#0D47A1')],
            foreground=[('active', 'white'), ('pressed', 'white')]
        )
        
        style.map(
            'TButton',
            background=[('active', '#616161'), ('pressed', '#424242')],
            foreground=[('active', 'white'), ('pressed', 'white')]
        )
    
    def count_words(self):
        text = self.text_input.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Warning", "Please enter some text first!")
            return
        
        # Count words (handling multiple spaces and newlines)
        words = re.findall(r'\b\w+\b', text)
        word_count = len(words)
        
        self.result_label.config(text=f"Total words: {word_count}")
    
    def next_action(self):
        # Clear the text input and result
        self.text_input.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.text_input.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordCounterApp(root)
    
    # Set dark theme for the root window
    root.configure(bg="#2d2d2d")
    
    root.mainloop()
