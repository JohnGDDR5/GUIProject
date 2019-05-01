import tkinter
from tkinter import *

def doBut1():
    label_1.configure(text = "pressed ONE")
    
def doBut2():
    label_1.configure(text = "pressed TWO")

def doBut3():
    label_1.configure(text = "pressed THREE")

def doBut4():
    label_1.configure(text = "pressed FOUR")
    
def doBut5():
    label_1.configure(text = "empty")

#"Pictures/Minecraft \- Creeper.png"
root = tkinter.Tk()
logo = tkinter.PhotoImage(file="Pictures/Minecraft - Creeper.png")

label_1 = tkinter.Label(root, text="empty", image=logo)
label_1.photo = logo
label_1.grid(row=0, column=0, columnspan=2)



but1 = tkinter.Button(root, text="ONE", command=doBut1, width=10)
but1.grid(row=1, column=0)

but2 = tkinter.Button(root, text="TWO", command=doBut2, width=10)
but2.grid(row=1, column=1)

but3 = tkinter.Button(root, text="THREE", command=doBut3, width=10)
but3.grid(row=2, column=0)

but4 = tkinter.Button(root, text="FOUR", command=doBut4, width=10)
but4.grid(row=2, column=1)

but5 = tkinter.Button(root, text="Reset", command=doBut5, width=10, bg="red")#, anchor = N)
but5["anchor"] = N
#Another way of changing more than one thing is .configure(text = "N")
but5.grid(row=1, column=2, columnspan=1, rowspan=2, padx=10, sticky= W+E+N+S)#, fill=X)
#but5.pack()
          
                    
root.mainloop()
