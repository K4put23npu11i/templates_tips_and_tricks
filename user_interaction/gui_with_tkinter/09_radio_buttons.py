# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=5262s

from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Radio Buttons")
root.iconbitmap('./data/icon.ico')

r = IntVar()  # Tkinter Variable
r.set(1)  # To set a first selection of radio button


def clicked(frame, value):
    myLabel = Label(frame, text=value)
    myLabel.pack()


# First version - specify each entry manually
frame1 = LabelFrame(root, text="First Version ...", padx=20, pady=20)  # Padding here is inside the frame
frame1.pack(padx=10, pady=20)  # Padding here is outside the frame
Radiobutton(frame1, text="Option1", variable=r, value=1, command=lambda:clicked(frame1, r.get())).pack()
Radiobutton(frame1, text="Option2", variable=r, value=2, command=lambda:clicked(frame1, r.get())).pack()


# Second version - loop over a list of tuples
frame2 = LabelFrame(root, text="Second Version ...", padx=20, pady=20)  # Padding here is inside the frame
frame2.pack(padx=10, pady=20)  # Padding here is outside the frame
MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Onion", "Onion"),
    ("Mushrooms", "Mushrooms")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(frame2, text=text, variable=pizza, value=mode).pack(anchor=W)

myButton = Button(frame2, text="Show value!", command=lambda: clicked(frame2, pizza.get()))
myButton.pack()

# Start gui and loop over it to react on changes
root.mainloop()
