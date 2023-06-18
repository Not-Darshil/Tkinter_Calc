import tkinter
from tkinter import *
def fx():
    print("crazy")

win=Tk()
win.geometry("500x500")
b1=Button(win, text="button1",padx=20,pady=20,command=fx)
b1.place(x=350,y=350)#coordinates
win.mainloop()
