import tkinter as tk
from tkinter import messagebox
import json
import os

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do List")

        self.tasks = self.load_tasks()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical")
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry_task = tk.Entry(root, width=50)
        self.entry_task.pack(pady=10)

        self.btn_add_task = tk.Button(root, text="Add Task", command=self.add_task)
        self.btn_add_task.pack(pady=5)

        self.btn_delete_task = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.btn_delete_task.pack(pady=5)

        self.btn_mark_completed = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.btn_mark_completed.pack(pady=5)

        self.load_tasks_to_listbox()

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

    def load_tasks_to_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = " (Done)" if task["completed"] else ""
            self.task_listbox.insert(tk.END, task["description"] + status)

    def add_task(self):
        task_description = self.entry_task.get()
        if task_description:
            self.tasks.append({"description": task_description, "completed": False})
            self.save_tasks()
            self.load_tasks_to_listbox()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.save_tasks()
            self.load_tasks_to_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def mark_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = not self.tasks[selected_task_index]["completed"]
            self.save_tasks()
            self.load_tasks_to_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()