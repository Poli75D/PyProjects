from tkinter import *
from time import strftime

root = Tk()
root.title("Digital System Clock")

def fun_Time():
    lbl.config(text = strftime("%H:%M:%S"))
    lbl.after(1000, fun_Time)

lbl = Label(root, font="arial 160 bold", bg="black", fg="white")
lbl.pack(anchor="center", fill="both", expand=1)

fun_Time()
mainloop()