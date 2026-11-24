import tkinter as tk
from tkinter import messagebox

def login():
    if user.get() == "admin" and pwd.get() == "1234":
        messagebox.showinfo("Login", "Welcome!")
    else:
        messagebox.showerror("Login", "Invalid credentials")

root = tk.Tk()
root.title("Login")
root.geometry("250x150")

tk.Label(root, text="Username").pack()
user = tk.Entry(root); user.pack()
tk.Label(root, text="Password").pack()
pwd = tk.Entry(root, show="*"); pwd.pack()
tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()