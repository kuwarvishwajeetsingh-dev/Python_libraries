import tkinter as tk

root = tk.Tk()                    # 1. create main window
root.title("My First App")        # 2. set title
root.geometry("1000x1000")          # 3. size: width x height

# 4. add widgets here
lbl = tk.Label(root, text="Hello Kuwar", 
               font=("Arial", 16), fg="black", bg="yellow")
lbl.pack()
def greet():
    print("Button clicked!")

btn = tk.Button(root, text="Click Me", command=greet, bg="green", 
                fg="white")
btn.pack()
entry = tk.Entry(root, width=30)
entry.pack()
value = entry.get()          # read text
entry.delete(0, tk.END)      # clear it
entry.insert(0, "default")   # set text
txt = tk.Text(root, height=10, width=50)
txt.pack()
content = txt.get("1.0", tk.END)  
var = tk.IntVar()
chk = tk.Checkbutton(root, text="I agree", variable=var)
chk.pack()
# var.get() returns 1 if checked, 0 if not # from line 1, char 0 to end
gender = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender, value="Female").pack()
lb = tk.Listbox(root)
for item in ["Python", "Java", "C", "C++", "JavaScript"]:
    lb.insert(tk.END, item)
lb.pack()
# lb.get(lb.curselection())  -> selected item
tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL).pack()
tk.Spinbox(root, from_=1, to=10).pack()
frame = tk.Frame(root, bg="lightgrey", padx=10, pady=10)
frame.pack()
tk.Label(frame, text="Inside frame").pack()
c = tk.Canvas(root, width=300, height=200, bg="white")
c.create_line(0, 0, 300, 200)
c.create_rectangle(50, 50, 150, 100, fill="red")
c.create_oval(100, 100, 200, 180, fill="blue")
c.create_text(150, 20, text="Canvas Demo")
c.pack()
root.mainloop()                   # 5. start the event loop
