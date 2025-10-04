import tkinter as tk
from tkinter import messagebox
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        result_label.config(text=f"BMI: {bmi:.2f} ({category})")
    except:
        messagebox.showerror("Error", "Please enter valid numbers!")
root = tk.Tk()
root.title("BMI Calculator")
tk.Label(root, text="Weight (kg):").grid(row=0, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1)
tk.Label(root, text="Height (m):").grid(row=1, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1)
tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=2, column=0, columnspan=2)
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)
root.mainloop()
