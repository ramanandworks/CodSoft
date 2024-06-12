import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password(length):
    if length < 1:
        return "Length must be at least 1"
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.label = tk.Label(root, text="Enter password length:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Generate Password", command=self.display_password)
        self.button.pack(pady=10)

        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack(pady=10)
        self.password_label.pack_forget()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def display_password(self):
        try:
            length = int(self.entry.get())
            password = generate_password(length)
            self.result_label.config(text=password)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number for the password length.")

root = tk.Tk()
app = PasswordGeneratorApp(root)

root.mainloop()