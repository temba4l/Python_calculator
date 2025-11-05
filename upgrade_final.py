import tkinter as tk
from tkinter import messagebox
import math

# -----------------------------
# Part 1: Calculator Functions
# -----------------------------

memory = 0
history = []
previous_result = None

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    result = a * b
    if a == 0 or b == 0:
        print("Multiplication by zero detected.")
    return result

def divide(a, b):
    if b == 0:
        messagebox.showerror("Error", "Division by zero!")
        return None
    return a / b

def modulus(a, b):
    if b == 0:
        messagebox.showerror("Error", "Modulus by zero!")
        return None
    return a % b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        messagebox.showerror("Error", "Square root of negative number!")
        return None
    return math.sqrt(a)

# -----------------------------
# Part 2: Memory Functions
# -----------------------------

def memory_add():
    global memory
    try:
        memory += float(entry_num1.get())
        messagebox.showinfo("Memory", f"Added to memory: {memory}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def memory_subtract():
    global memory
    try:
        memory -= float(entry_num1.get())
        messagebox.showinfo("Memory", f"Subtracted from memory: {memory}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def memory_recall():
    entry_num1.delete(0, tk.END)
    entry_num1.insert(0, str(memory))

def memory_clear():
    global memory
    memory = 0
    messagebox.showinfo("Memory", "Memory cleared.")

# -----------------------------
# Part 3: History and Result Handling
# -----------------------------

def update_history(num1, operation, num2, result):
    history.append(f"{num1} {operation} {num2} = {result}")

def display_history():
    hist_window = tk.Toplevel(root)
    hist_window.title("Calculation History")
    if not history:
        tk.Label(hist_window, text="No calculations yet.").pack()
    else:
        for calc in history:
            tk.Label(hist_window, text=calc).pack(anchor="w")

def clear_history():
    global history
    history.clear()
    messagebox.showinfo("Info", "History cleared.")

# -----------------------------
# Part 4: GUI and Calculation Logic
# -----------------------------

def calculate():
    global previous_result
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operation_var.get()

        if op == "+":
            result = add(num1, num2)
        elif op == "-":subtract (a,b)
            result = a-b
        elif op == "*":print(f"subtracting{a}-{b}={result}")
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
        elif op == "%":
            result = modulus(num1, num2)
        elif op == "^":
            result = power(num1, num2)
        elif op == "sqrt":
            result = sqrt(num1)
            num2 = 0  # For history, since sqrt is unary
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return

        if result is not None:
            result_label.config(text=f"Result: {result}")
            update_history(num1, op, num2, result)
            previous_result = result

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def use_previous_result():
    if previous_result is not None:
        entry_num1.delete(0, tk.END)
        entry_num1.insert(0, str(previous_result))

# -----------------------------
# Part 5: GUI Setup
# -----------------------------

root = tk.Tk()
root.title("Advanced Python Calculator")

# Input fields
tk.Label(root, text="First Number:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="Second Number:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# Operation selection
tk.Label(root, text="Operation:").grid(row=2, column=0)
operation_var = tk.StringVar(value="+")
operations = ["+", "-", "*", "/", "%", "^", "sqrt"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=2, column=1)

# Buttons
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=5)

history_button = tk.Button(root, text="Show History", command=display_history)
history_button.grid(row=4, column=0, pady=5)

clear_button = tk.Button(root, text="Clear History", command=clear_history)
clear_button.grid(row=4, column=1, pady=5)

# Memory buttons
memory_frame = tk.Frame(root)
memory_frame.grid(row=5, column=0, columnspan=2, pady=5)

tk.Button(memory_frame, text="M+", command=memory_add).pack(side=tk.LEFT)
tk.Button(memory_frame, text="M-", command=memory_subtract).pack(side=tk.LEFT)
tk.Button(memory_frame, text="MR", command=memory_recall).pack(side=tk.LEFT)
tk.Button(memory_frame, text="MC", command=memory_clear).pack(side=tk.LEFT)

# Previous result button
prev_result_button = tk.Button(root, text="Use Previous Result", command=use_previous_result)
prev_result_button.grid(row=6, column=0, columnspan=2, pady=5)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=7, column=0, columnspan=2)

# Run the application
root.mainloop()
