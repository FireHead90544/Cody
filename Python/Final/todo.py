import json
import os
import sys

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    try:
        os.system("python -m pip install tk")
    except:
        print("Library not found, install it using 'pip install tk'")
        sys.exit()

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_task_list()
        entry.delete(0, tk.END)

def update_task_list():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        listbox.insert(tk.END, f"{i+1}. {task['task']} [{status}]")

def complete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = not tasks[index]["completed"]
        update_task_list()
        save_tasks()

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        update_task_list()
        save_tasks()

# Create the main window
root = tk.Tk()
root.title("To-Do | Do-Too?")
root.geometry("400x500")
root.resizable(False, False)

# Style configuration
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 14))
style.configure("TEntry", font=("Helvetica", 12), padding=10)
style.configure("TListbox", font=("Helvetica", 12))

# Create UI elements
entry_label = ttk.Label(root, text="Enter a new task:")
entry_label.pack(pady=10)

entry = ttk.Entry(root, width=50)
entry.pack(pady=10)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

add_button = ttk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

complete_button = ttk.Button(button_frame, text="Complete Task", command=complete_task)
complete_button.grid(row=0, column=1, padx=5)

delete_button = ttk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

listbox_label = ttk.Label(root, text="Tasks:")
listbox_label.pack(pady=10)

listbox = tk.Listbox(root, width=50, height=15, font=("Helvetica", 12))
listbox.pack(pady=10)


tasks = load_tasks()
update_task_list()

# Main Loop
root.mainloop()

