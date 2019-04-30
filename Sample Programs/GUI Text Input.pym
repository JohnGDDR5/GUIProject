
import tkinter as tk
#import tkFont
from tkinter import *
from tkinter.ttk import *

#Functions
def doBut1():
    label_1.configure(text = "Name: "+ txt.get())
    
window = tk.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

label_1 = tk.Label(window, width=25, text="Name: ")
label_1.grid(row=0, column=0, columnspan=2)

txt = Entry(window, width=25)
txt.grid(row=1, column=0)

but1 = tk.Button(window, text="ONE", command=doBut1, width=25, font=("Arial Bold", 10))
but1.grid(row=2, column=0)


chk = Checkbutton(window, text='Choose', var=False)
chk.grid(row=3, column=0)

window.mainloop()

"""import tkinter as tk

from tkinter import * 
#import tkinter as tk

#Functions
def doBut1():
    #name = "Juan"
    label_1.configure(text = "Name: "+ txt.get())

window = tk.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

label_1 = tk.Label(window, text="Text: ", width=25)#, font=("Arial Bold", 10))
label_1.grid(row=0, column=0)

txt = Entry(window,width=10)
txt.grid(row=1, column=0)
#label_1.grid(row=0, column=0, columnspan=1)

but1 = tk.Button(window, text="Click To Set Text", command=doBut1, width=25, font=("Arial Bold", 10))
but1.grid(row=2, column=0)
                    
window.mainloop()"""
