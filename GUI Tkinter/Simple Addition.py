import tkinter as tk

def add():
    result = int(e1.get()) + int(e2.get())
    lbl_result.config(text="Sum = " + str(result))

root = tk.Tk()
root.title("Adder")
root.geometry("600x600")

tk.Label(root, text="Number 1").grid(row=0, column=0)
tk.Label(root, text="Number 2").grid(row=1, column=0)
e1 = tk.Entry(root); e1.grid(row=0, column=1)
e2 = tk.Entry(root); e2.grid(row=1, column=1)

tk.Button(root, text="Add", command=add).grid(row=2, column=0, columnspan=2)
lbl_result = tk.Label(root, text="")
lbl_result.grid(row=3, column=0, columnspan=2)

root.mainloop()