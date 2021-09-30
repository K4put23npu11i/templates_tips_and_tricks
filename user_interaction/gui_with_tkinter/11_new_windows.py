# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=5262s

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os

root = Tk()
root.title("First window")
root.iconbitmap('./data/icon.ico')


def open():
    global my_img
    top = Toplevel()
    top.title("Second window")
    top.iconbitmap('./data/icon.ico')
    lbl = Label(top, text="Hello World").pack()
    all_image_paths = os.listdir('./data/images/')
    my_img = ImageTk.PhotoImage(Image.open('./data/images/' + all_image_paths[0]))
    lbl2 = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close second window", command=top.destroy).pack()


btn = Button(root, text="Open second window", command=open).pack()

# Start gui and loop over it to react on changes
root.mainloop()
