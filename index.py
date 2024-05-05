from tkinter import *

root = Tk()
root.title("Calculator")
#root.geometry("500x500")

windowEntry = Entry(root,width=35,borderwidth=5)
windowEntry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_Click(number):
    windowEntry.insert(0,number)

button_0 = Button(root,text="0",padx=40,pady=20,command=lambda:button_Click(0))
button_1 = Button(root,text="1",padx=40,pady=20,command=lambda:button_Click(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda:button_Click(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda:button_Click(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda:button_Click(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda:button_Click(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda:button_Click(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda:button_Click(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda:button_Click(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda:button_Click(9))
button_addd =Button(root,text="+",padx=39,pady=20,command=lambda:button_Click()) 
button_equal = Button(root,text="=",padx=100,pady=20,command=lambda:button_Click(),anchor=N)
button_clear = Button(root,text="Clear",padx=79,pady=20,command=lambda:button_Click())

#placing buttons on the screen 
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_addd.grid(row=4,column=1)
button_equal.grid(row=5,column=0,columnspan=2)
button_clear.grid(row=5,column=1,columnspan=2)
root.mainloop()