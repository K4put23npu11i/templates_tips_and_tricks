# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=5262s

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
from tkinter import filedialog

root = Tk()
root.title("File Dialog")
root.iconbitmap('./data/icon.ico')


def open_file():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="./data/images", title="Select a File",
                                               filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"),
                                                          ("all files", "*.*"))
                                               )

    myLabel = Label(root, text=root.filename)
    myLabel.pack()

    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_Label = Label(image=my_image).pack()


def open_dir():
    root.dirname = filedialog.askdirectory()

    myLabel_dir = Label(root, text=root.dirname)
    myLabel_dir.pack()


btn_file = Button(root, text="Open file", command=open_file).pack()

btn_dir = Button(root, text="Open directory", command=open_dir).pack()


# Start gui and loop over it to react on changes
root.mainloop()
