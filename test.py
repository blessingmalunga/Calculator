from tkinter import *

def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def clear():
    e.delete(0, END)

def calculate():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, result)
    except Exception:
        e.delete(0, END)
        e.insert(0, "Error")

root = Tk()
root.title("Calculator")
root.config(bg="black")
root.geometry("300x275")

e = Entry(root, width=50, bd=1, font=("Arial", 16))
e.grid(row=0, column=0, columnspan=4, pady=10)


# Number Buttons
b1 = Button(root, text="1", font=("Arial", 24), command=lambda: button_click(1))
b1.grid(row=1, column=0, padx=0, pady=5)
b2 = Button(root, text="2", font=("Arial", 24), command=lambda: button_click(2))
b2.grid(row=1, column=1, padx=0, pady=5)
b3 = Button(root, text="3", font=("Arial", 24), command=lambda: button_click(3))
b3.grid(row=1, column=2, padx=0, pady=5)
b4 = Button(root, text="4", font=("Arial", 24), command=lambda: button_click(4))
b4.grid(row=2, column=0, padx=0, pady=5)
b5 = Button(root, text="5", font=("Arial", 24), command=lambda: button_click(5))
b5.grid(row=2, column=1, padx=0, pady=5)
b6 = Button(root, text="6", font=("Arial", 24), command=lambda: button_click(6))
b6.grid(row=2, column=2, padx=0, pady=5)
b7 = Button(root, text="7", font=("Arial", 24), command=lambda: button_click(7))
b7.grid(row=3, column=0, padx=0, pady=5)
b8 = Button(root, text="8", font=("Arial", 24), command=lambda: button_click(8))
b8.grid(row=3, column=1, padx=0, pady=5)
b9 = Button(root, text="9", font=("Arial", 24), command=lambda: button_click(9))
b9.grid(row=3, column=2, padx=0, pady=5)
b0 = Button(root, text="0", font=("Arial", 24), command=lambda: button_click(0))
b0.grid(row=4, column=0, padx=0, pady=5)

# Operator Buttons
b_plus = Button(root, text="+", font=("Arial", 24), command=lambda: button_click("+"))
b_plus.grid(row=1, column=3, padx=0, pady=5)
b_minus = Button(root, text="-", font=("Arial", 24), command=lambda: button_click("-"))
b_minus.grid(row=2, column=3, padx=0, pady=5)
b_multiply = Button(root, text="*", font=("Arial", 24), command=lambda: button_click("*"))
b_multiply.grid(row=3, column=3, padx=0, pady=5)
b_divide = Button(root, text="/", font=("Arial", 24), command=lambda: button_click("/"))
b_divide.grid(row=4, column=3, padx=0, pady=5)

# Other Buttons
b_clear = Button(root, text="C", font=("Arial", 24), command=clear)
b_clear.grid(row=4, column=1, padx=0, pady=5)
b_period = Button(root, text=".", font=("Arial", 24), command=lambda: button_click("."))
b_period.grid(row=4, column=2, padx=0, pady=5)
b_equals = Button(root, text="=", font=("Arial", 24), command=calculate)
b_equals.grid(row=5, column=0, columnspan=4, padx=0, pady=5)

root.mainloop()
