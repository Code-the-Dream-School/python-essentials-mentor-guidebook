import tkinter as tk
from tkinter import messagebox

# Sample local JSON-like employee data
employees = [
    {"name": "Alice Johnson", "title": "Software Engineer", "department": "Engineering"},
    {"name": "Bob Smith", "title": "Product Manager", "department": "Product"},
    {"name": "Cathy Lin", "title": "UX Designer", "department": "Design"},
    {"name": "Derek Tran", "title": "Data Analyst", "department": "Data"},
    {"name": "Ella Zhang", "title": "DevOps Engineer", "department": "Infrastructure"}
]

current_index = 0

# Create the main window
root = tk.Tk()
root.title("Tkinter Demo with Employee Directory")
root.geometry("1080x600")
root.configure(bg="#f0f0f0")


# Function to update label text
def greet_user():
    name = entry.get()
    if name.strip() == "":
        messagebox.showwarning("Input Error", "Please enter your name.")
    else:
        label_result.config(text=f"Hello, {name}!")

# Function to show next employee
def show_next_employee():
    global current_index
    current_index = (current_index + 1) % len(employees)
    show_employee(current_index)

# Function to show previous employee
def show_previous_employee():
    global current_index
    current_index = (current_index - 1) % len(employees)
    show_employee(current_index)

# Function to display current employee info
def show_employee(index):
    employee = employees[index]
    emp_info = f"Name: {employee['name']}\nTitle: {employee['title']}\nDepartment: {employee['department']}"
    api_result.config(text=emp_info)

# Title label
title = tk.Label(root, text="Tkinter Demo with Employee Directory",
                 font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")
title.pack(pady=20)

# Input label
label = tk.Label(root, text="Enter your name:", font=("Arial", 14), bg="#f0f0f0")
label.pack(pady=10)

# Entry widget
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=5)

# Frame for buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=15)

# Greet Button
button = tk.Button(button_frame, text="Greet Me", command=greet_user,
                   font=("Arial", 12), bg="#4CAF50", fg="white", width=12)
button.grid(row=0, column=0, padx=10)

# Show Previous Button
prev_button = tk.Button(button_frame, text="Previous", command=show_previous_employee,
                        font=("Arial", 12), bg="#9E9E9E", fg="white", width=12)
prev_button.grid(row=0, column=1, padx=10)

# Show Next Button
next_button = tk.Button(button_frame, text="Next", command=show_next_employee,
                        font=("Arial", 12), bg="#2196F3", fg="white", width=12)
next_button.grid(row=0, column=2, padx=10)

# Result label for greeting
label_result = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="#555", bg="#f0f0f0")
label_result.pack(pady=10)

# Employee directory display
api_result = tk.Label(root, text="", font=("Arial", 13), fg="#444",
                      wraplength=800, justify="center", bg="#f0f0f0")
api_result.pack(pady=20)

# Show first employee on load
show_employee(current_index)

# Quit Button
quit_btn = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 12),
                     bg="#f44336", fg="white", width=12)
quit_btn.pack(side="bottom", pady=20)

# Run the app
root.mainloop()
