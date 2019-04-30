
import tkinter as tk
#import tkFont
from tkinter import *
from tkinter.ttk import *

window = tk.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

selected1 = IntVar()
selected1.set(1)

def clicked():
    label_1.configure(text = "Radio: "+str(selected1.get()))

rad1 = Radiobutton(window, text='Radiobutton 1', value=1, variable=selected1, command=clicked)
rad2 = Radiobutton(window, text='Radiobutton 2', value=2, variable=selected1, command=clicked)
rad3 = Radiobutton(window, text='Radiobutton 3', value=3, variable=selected1, command=clicked)

rad1.grid(row=1, column=0)
rad2.grid(row=2, column=0)
rad3.grid(row=3, column=0)

#Radio Label
label_1 = tk.Label(window, text="Radio: "+str(selected1.get()))
label_1.grid(row=4, column=0, columnspan=2)

chk1_state = BooleanVar()
chk1_state.set(True)

chk2_state = BooleanVar()
chk2_state.set(True)

chk3_state = BooleanVar()
chk3_state.set(True)

stateList = [BooleanVar(), BooleanVar(), BooleanVar()]
stateList[0].set(True)
stateList[1].set(True)
stateList[2].set(True)

def clickedCheck():
    label_3.configure(text = "Test: "+str([stateList[0].get(), stateList[1].get(), stateList[2].get()]))

chk1 = Checkbutton(window, text='Checkbox 1', var=stateList[0], command=clickedCheck)
chk1.grid(row=5, column=0)

chk2 = Checkbutton(window, text='Checkbox 2', var=stateList[1], command=clickedCheck)
chk2.grid(row=6, column=0)

chk3 = Checkbutton(window, text='Checkbox 3', var=stateList[2], command=clickedCheck)
chk3.grid(row=7, column=0)

#CheckBox Label
label_2 = tk.Label(window, text="CheckBoxes: "+str(list(stateList)))
label_2.grid(row=8, column=0, columnspan=2)
label_3 = tk.Label(window, text="Test: "+str([stateList[0].get(), stateList[1].get(), stateList[2].get()]))
label_3.grid(row=9, column=0, columnspan=2)

window.mainloop()
