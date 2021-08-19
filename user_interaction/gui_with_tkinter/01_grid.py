# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=632s

from tkinter import *

root = Tk()

# set properties to whole application
canvas = Canvas(root, width=600, height=300)

# Create the widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Nex Text in second Label Widget")

# Put it on the Screen
# myLabel1.pack()  # Puts the widget where space is available
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# Start gui and loop over it to react on changes
root.mainloop()
