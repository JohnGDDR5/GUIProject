from tkinter import*

master=Tk()
master.geometry("400x450")

frame0=Frame(master, width=400, height=150, background="Cyan")
frame0.grid(row=0, column=0, columnspan=2, sticky= W+E+N+S)

frame1=Frame(master, width=200, height=150, background="Blue")
frame1.grid(row=1, column=0, sticky= W+E+N+S)

frame2=Frame(master, width=200, height=150, background="Red")
frame2.grid(row=2, column=0, sticky= W+E+N+S)

frame3=Frame(master, width=200, height=150, background="Green")
frame3.grid(row=1, column=1, sticky= W+E+N+S)

frame4=Frame(master, width=200, height=150, background="Yellow")
frame4.grid(row=2, column=1, sticky= W+E+N+S)


#range(2) is (0,1)
for i in range(3):
    #if i != 0:
    Grid.rowconfigure(master, i, weight=2)
    #This prevents from adding a columnconfigure(2), since there are only columns 0 & 1, not 2, Which messes up the expanding
    if i != 2:
        Grid.columnconfigure(master, i, weight=2)

master.mainloop()