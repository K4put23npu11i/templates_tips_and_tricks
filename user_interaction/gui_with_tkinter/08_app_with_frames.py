# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=5262s

from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Simple Image Viewer")
root.iconbitmap('./data/icon.ico')

frame = LabelFrame(root, text="This is my Frame ...", padx=50, pady=50)  # Padding here is inside the frame
frame.pack(padx=10, pady=20)  # Padding here is outside the frame

# b = Button(frame, text="Don't click here!!")
# b.pack()

# Normally you can only use grid or pack. But inside a frame you can create a "new" grid
b = Button(frame, text="Don't click here!!")
b.grid(row=0, column=0)
b2 = Button(frame, text="Don't click here!!")
b2.grid(row=1, column=1)

# Start gui and loop over it to react on changes
root.mainloop()
