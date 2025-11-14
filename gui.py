import tkinter as tk
from todo import ToDoList

todo = ToDoList()

def add_task():
    task = entry.get()
    try:
        todo.add_task(task)
        update_listbox()
        entry.delete(0, tk.END)
    except ValueError as e:
        status_label.config(text=str(e))

def delete_task():
    try:
        selected = listbox.curselection()
        if not selected:
            raise IndexError("No task selected")
        todo.delete_task(selected[0])
        update_listbox()
    except Exception as e:
        status_label.config(text=str(e))

def update_listbox():
    listbox.delete(0, tk.END)
    for task in todo.get_tasks():
        listbox.insert(tk.END, task)

root = tk.Tk()
root.title("Simple To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_button.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

status_label = tk.Label(root, text="", fg="red")
status_label.pack()

root.mainloop()
