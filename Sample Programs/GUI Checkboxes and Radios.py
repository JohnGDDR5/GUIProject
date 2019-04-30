
import tkinter as tk
#import tkFont
from tkinter import *
from tkinter.ttk import *

window = tk.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

#Radio Stuff
selected = IntVar()
selected.set(1)

def clicked():
    label_1.configure(text = "Radio: "+str(selected.get()))

rad1 = Radiobutton(window,text='Radiobutton 1', value=1, variable=selected, command=clicked)
rad2 = Radiobutton(window,text='Radiobutton 2', value=2, variable=selected, command=clicked)
rad3 = Radiobutton(window,text='Radiobutton 3', value=3, variable=selected, command=clicked)

rad1.grid(row=1, column=0)
rad2.grid(row=2, column=0)
rad3.grid(row=3, column=0)

#Radio Label
label_1 = tk.Label(window, text="Radio: ")#+selected.get())
label_1.grid(row=4, column=0, columnspan=2)

#CheckButton
chk1_state = BooleanVar()
chk1_state.set(True)

chk2_state = BooleanVar()
chk2_state.set(True)

chk3_state = BooleanVar()
chk3_state.set(True)

def clickedCheck():
    label_2.configure(text = "CheckBoxes: "+"["+str(chk1_state.get())+","+str(chk2_state.get())+","+str(chk3_state.get())+"]")

chk1 = Checkbutton(window, text='Checkbox 1', var=chk1_state, command=clickedCheck)
chk1.grid(row=5, column=0)

chk2 = Checkbutton(window, text='Checkbox 2', var=chk2_state, command=clickedCheck)
chk2.grid(row=6, column=0)

chk3 = Checkbutton(window, text='Checkbox 3', var=chk3_state, command=clickedCheck)
chk3.grid(row=7, column=0)

#CheckBox Label
label_2 = tk.Label(window, text="CheckBoxes: [True, True, True]")#+selected.get())
label_2.grid(row=8, column=0, columnspan=2)

window.mainloop()
