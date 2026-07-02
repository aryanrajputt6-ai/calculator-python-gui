from tkinter import *

root = Tk()
root.title("Pro Calculator")
root.geometry("340x500")
root.configure(bg="#121212")

# Display
entry = Entry(root, font=("Segoe UI", 24), bg="#1e1e1e", fg="white",
              borderwidth=0, justify="right")
entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

# Functions
def press(value):
    entry.insert(END, value)

def clear():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button style
def create_button(text, row, col, cmd, bg="#2d2d2d"):
    Button(frame, text=text, command=cmd,
           font=("Segoe UI", 14),
           fg="white", bg=bg,
           activebackground="#444",
           width=5, height=2, bd=0)\
        .grid(row=row, column=col, padx=5, pady=5)

# Frame for buttons
frame = Frame(root, bg="#121212")
frame.pack()

# Row 1
create_button("C", 0, 0, clear, "#d32f2f")
create_button("⌫", 0, 1, backspace, "#616161")
create_button("%", 0, 2, lambda: press("%"))
create_button("/", 0, 3, lambda: press("/"), "#ff9800")

# Row 2
create_button("7", 1, 0, lambda: press("7"))
create_button("8", 1, 1, lambda: press("8"))
create_button("9", 1, 2, lambda: press("9"))
create_button("*", 1, 3, lambda: press("*"), "#ff9800")

# Row 3
create_button("4", 2, 0, lambda: press("4"))
create_button("5", 2, 1, lambda: press("5"))
create_button("6", 2, 2, lambda: press("6"))
create_button("-", 2, 3, lambda: press("-"), "#ff9800")

# Row 4
create_button("1", 3, 0, lambda: press("1"))
create_button("2", 3, 1, lambda: press("2"))
create_button("3", 3, 2, lambda: press("3"))
create_button("+", 3, 3, lambda: press("+"), "#ff9800")

# Row 5
create_button("0", 4, 0, lambda: press("0"))
create_button(".", 4, 1, lambda: press("."))
create_button("=", 4, 2, calculate, "#4caf50")

# Keyboard support
def key_event(event):
    key = event.char
    if key in "0123456789+-*/.":
        press(key)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        backspace()

root.bind("<Key>", key_event)

root.mainloop()