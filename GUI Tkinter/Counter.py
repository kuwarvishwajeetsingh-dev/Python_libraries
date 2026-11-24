import tkinter as tk

count = 0
def increment():
    global count
    count += 1
    lbl.config(text=count)

root = tk.Tk()
lbl = tk.Label(root, text=0, font=("Arial", 30)).pack()

tk.Button(root, text="Increase", command=increment).pack()
root.mainloop()