import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    try:
        length = int(entry_length.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
    except:
        messagebox.showerror("Error", "Enter a valid number!")
root = tk.Tk()
root.title("Random Password Generator")
tk.Label(root, text="Password Length:").grid(row=0, column=0)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1)
tk.Button(root, text="Generate Password", command=generate_password).grid(row=1, column=0, columnspan=2)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=2, column=0, columnspan=2)
root.mainloop()
