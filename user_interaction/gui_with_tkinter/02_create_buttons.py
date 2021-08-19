# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=1169s

from tkinter import *

root = Tk()

# set properties to whole application
canvas = Canvas(root, width=600, height=300)


def my_click():
    my_label1 = Label(root, text="I clicked a button!")
    my_label1.grid(row=1, column=2)


# Create button widget
myButton = Button(root, text="Click me!")
myButton2 = Button(root, text="Click me!", state=DISABLED)
myButton3 = Button(root, text="Click me!", padx=50, pady=50, fg="blue", bg="red")  # also hex colors are working
myButton4 = Button(root, text="Click me!", command=my_click)  # Do not include () after the function!


# Put it on the Screen
myButton.grid(row=0, column=0)
myButton2.grid(row=0, column=1)
myButton3.grid(row=0, column=2)
myButton4.grid(row=1, column=1)

# Start gui and loop over it to react on changes
root.mainloop()
