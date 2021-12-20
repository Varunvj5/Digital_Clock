from tkinter import Tk
from tkinter import Label
import time
import sys


master = Tk()
master.title("Clock")

clock = Label(master, font=("Arial", 100), fg="cyan", bg="black")
clock.pack()


def gettime():
    timevar = time.strftime("%I:%M:%S")
    clock.config(text=timevar)
    clock.after(100, gettime)


gettime()

master.mainloop()
