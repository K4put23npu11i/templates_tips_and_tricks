# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=4699s

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to build a GUI")
root.iconbitmap('./data/icon.ico')

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open('./data/images/panda.jpg'))
my_label = Label(image=my_img)
my_label.pack()

# Start gui and loop over it to react on changes
root.mainloop()
