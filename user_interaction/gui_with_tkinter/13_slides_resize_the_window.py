# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=5262s

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
from tkinter import filedialog

root = Tk()
root.title("Sliders")
root.iconbitmap('./data/icon.ico')


def resize():
    new_size = str(hor_slider.get()) + "x" + str(vert_slider.get())

    label = Label(root, text=f"New size is: {new_size}").pack()

    root.geometry(new_size)


vert_slider = Scale(root, from_=300, to=600)
vert_slider.pack()

hor_slider = Scale(root, from_=300, to=600, orient="horizontal")
hor_slider.pack()

btn = Button(root, text="Resize the window", command=resize).pack()

# Start gui and loop over it to react on changes
root.mainloop()
