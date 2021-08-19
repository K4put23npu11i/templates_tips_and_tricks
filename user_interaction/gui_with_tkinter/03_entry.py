# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=1770s

from tkinter import *

root = Tk()

# set properties to whole application
canvas = Canvas(root, width=600, height=300)

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name here: ...")


def my_click():
    name = e.get()
    txt = f"Hello {name}"
    my_label1 = Label(root, text=txt)
    my_label1.pack()


myButton = Button(root, text="Enter Name", command=my_click)  # Do not include () after the function!


# Put it on the Screen
myButton.pack()


# Start gui and loop over it to react on changes
root.mainloop()
