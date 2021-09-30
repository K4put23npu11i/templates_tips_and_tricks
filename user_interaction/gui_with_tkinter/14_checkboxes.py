# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=5262s

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
from tkinter import filedialog

root = Tk()
root.title("Checkboxes")
root.iconbitmap('./data/icon.ico')


def show():
    myLabel = Label(root, text=var.get()).pack()


var = IntVar()

c = Checkbutton(root, text="Check this box", variable=var)
# c.select()
c.pack()

# var = StringVar()
#
# c = Checkbutton(root, text="Check this box", variable=var, onvalue="ON VALUE", offvalue="OFF VALUE")
# c.deselect()
# c.pack()


btn = Button(root, text="Show Selection", command=show).pack()

# Start gui and loop over it to react on changes
root.mainloop()
