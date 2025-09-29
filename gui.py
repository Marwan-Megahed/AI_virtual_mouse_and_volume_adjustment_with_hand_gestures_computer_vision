import tkinter as tk
from tkinter import ttk
import ai_virtual_mouse_project_scroll_volume as project
from tkinter import messagebox



def start_app():
    intro.destroy()
    project.run_virtual_mouse()

def exit_app():
    intro.destroy()

# Create intro window
intro = tk.Tk()
intro.title("Virtual Mouse App")
intro.geometry("600x400")
intro.configure(bg="#2C2F33")  # Dark background
intro.resizable(False, False)

# Style
style = ttk.Style(intro)
style.configure("TButton",
                font=("Segoe UI", 12, "bold"),
                padding=10)
style.map("TButton",
          background=[("active", "#99AAB5")])

# Title
title = tk.Label(intro,
                 text="🖱️ Virtual Mouse App",
                 font=("Segoe UI", 20, "bold"),
                 bg="#2C2F33",
                 fg="#FFFFFF")
title.pack(pady=20)

# Info
info = tk.Label(intro,
                text="Control your computer using hand gestures!\n\n"
                     "- Move cursor with index finger\n"
                     "- Pinch index + middle to click\n"
                     "- Use thumb + index + middle to scroll\n\n"
                     "Press Start to begin or Exit to quit.",
                font=("Segoe UI", 11),
                bg="#2C2F33",
                fg="#CCCCCC",
                justify="center")
info.pack(pady=10)

# Buttons
btn_frame = tk.Frame(intro, bg="#2C2F33")
btn_frame.pack(pady=20)

start_btn = ttk.Button(btn_frame, text="🚀 Start", command=start_app)
start_btn.grid(row=0, column=0, padx=20)

exit_btn = ttk.Button(btn_frame, text="❌ Exit", command=exit_app)
exit_btn.grid(row=0, column=1, padx=20)

intro.mainloop()