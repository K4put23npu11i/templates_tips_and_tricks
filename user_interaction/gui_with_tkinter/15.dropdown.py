# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=5262s

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
from tkinter import filedialog

root = Tk()
root.title("Dropdown Boxes")
root.iconbitmap('./data/icon.ico')
root.geometry("400x400")


options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()
var.set("Select something...")
# var.set(options[0])

drop = OptionMenu(root, var, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
drop = OptionMenu(root, var, *options)
drop.pack()

btn = Button(root, text="Show Selection", command=show).pack()

# Start gui and loop over it to react on changes
root.mainloop()
