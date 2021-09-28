# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=5262s

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")
root.iconbitmap('./data/icon.ico')


def info_popup():
    response = messagebox.showinfo("Header of showinfo popup", "Message of showinfo Popup")
    Label(root, text="showinfo popup returns: " + str(response)).pack()


def warning_popup():
    response = messagebox.showwarning("Header of showwarning popup", "Message of showwarning Popup")
    Label(root, text="showwarning popup returns: " + str(response)).pack()


def error_popup():
    response = messagebox.showerror("Header of showerror popup", "Message of showerror Popup")
    Label(root, text="showerror popup returns: " + str(response)).pack()


def ask_popup():
    response = messagebox.askquestion("Header of askquestion popup", "Message of askquestion Popup")
    Label(root, text="askquestion popup returns: " + str(response)).pack()


def ok_popup():
    response = messagebox.askokcancel("Header of askokcancel popup", "Message of askokcancel Popup")
    Label(root, text="askokcancel popup returns: " + str(response)).pack()


def yesno_popup():
    response = messagebox.askyesno("Header of askyesno popup", "Message of askyesno Popup")
    Label(root, text="askyesno popup returns: " + str(response)).pack()


myButton_info = Button(root, text="Info popup", command=info_popup).pack()
myButton_warning = Button(root, text="Warning popup", command=warning_popup).pack()
myButton_error = Button(root, text="Error popup", command=error_popup).pack()
myButton_ask = Button(root, text="Ask popup", command=ask_popup).pack()
myButton_okcancel = Button(root, text="OK popup", command=ok_popup).pack()
myButton_yesno = Button(root, text="Yes/No popup", command=yesno_popup).pack()

# Start gui and loop over it to react on changes
root.mainloop()
