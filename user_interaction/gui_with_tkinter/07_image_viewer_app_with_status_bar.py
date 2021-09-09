# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=5262s

from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Simple Image Viewer")
root.iconbitmap('./data/icon.ico')

global idx
global images


def go_left():
    global idx
    global images
    global image_label
    idx -= 1
    # print(idx)

    image_label.grid_forget()
    image_label = Label(image=images[idx])
    image_label.grid(row=0, column=0, columnspan=3)

    if idx == 0:
        button_left = Button(root, text="<<", state=DISABLED)
        button_left.grid(row=1, column=0)

    button_right = Button(root, text=">>", command=go_right)
    button_right.grid(row=1, column=2)

    status = Label(root, text=f"Image {idx + 1} of {len(images)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def go_right():
    global idx
    global images
    global image_label
    idx += 1
    # print(idx)

    image_label.grid_forget()
    image_label = Label(image=images[idx])
    image_label.grid(row=0, column=0, columnspan=3)

    if idx == len(images)-1:
        button_right = Button(root, text=">>", state=DISABLED)
        button_right.grid(row=1, column=2)

    button_left = Button(root, text="<<", command=go_left)
    button_left.grid(row=1, column=0)

    status = Label(root, text=f"Image {idx + 1} of {len(images)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)



idx = 0
images = []
for img in os.listdir('./data/images/'):
    path = './data/images/' + img
    my_img = ImageTk.PhotoImage(Image.open(path))
    images.append(my_img)

status = Label(root, text=f"Image {idx+1} of {len(images)}", bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

image_label = Label(image=images[0])
image_label.grid(row=0, column=0, columnspan=3)

button_left = Button(root, text="<<", state=DISABLED)
button_left.grid(row=1, column=0)

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=1, column=1, pady=10)

button_right = Button(root, text=">>", command=go_right)
button_right.grid(row=1, column=2)

# Start gui and loop over it to react on changes
root.mainloop()
