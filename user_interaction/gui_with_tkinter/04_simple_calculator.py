# Tkinter Course - Create Graphic User Interfaces in Python Tutorial - https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *

root = Tk()
root.title("Simple Calculator")

# set properties to whole application
canvas = Canvas(root, width=600, height=300)

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

global f_num
global sign
f_num = 0
sign = ""


def button_click_numbers(number):
    current = e.get()
    new = str(current) + str(number)
    e.delete(0, END)
    e.insert(0, new)
    return None


def button_click_result():
    global sign
    global f_num
    s_num = int(e.get())

    if sign == "+":
        result = f_num + s_num
    elif sign == "-":
        result = f_num - s_num
    elif sign == "*":
        result = f_num * s_num
    elif sign == "/":
        result = f_num / s_num
    else:
        print("PROBLEM!!")
        result = None

    e.delete(0, END)
    e.insert(0, result)
    return None


def button_click_clear():
    e.delete(0, END)


def button_click_add():
    global sign
    global f_num
    sign = "+"
    f_num = int(e.get())
    e.delete(0, END)


def button_click_sub():
    global sign
    global f_num
    sign = "-"
    f_num = int(e.get())
    e.delete(0, END)


def button_click_mul():
    global sign
    global f_num
    sign = "*"
    f_num = int(e.get())
    e.delete(0, END)


def button_click_div():
    global sign
    global f_num
    sign = "/"
    f_num = int(e.get())
    e.delete(0, END)


Btn_1 = Button(root, text="1", padx=35, pady=20, command=lambda: button_click_numbers(1))
Btn_2 = Button(root, text="2", padx=35, pady=20, command=lambda: button_click_numbers(2))
Btn_3 = Button(root, text="3", padx=35, pady=20, command=lambda: button_click_numbers(3))
Btn_4 = Button(root, text="4", padx=35, pady=20, command=lambda: button_click_numbers(4))
Btn_5 = Button(root, text="5", padx=35, pady=20, command=lambda: button_click_numbers(5))
Btn_6 = Button(root, text="6", padx=35, pady=20, command=lambda: button_click_numbers(6))
Btn_7 = Button(root, text="7", padx=35, pady=20, command=lambda: button_click_numbers(7))
Btn_8 = Button(root, text="8", padx=35, pady=20, command=lambda: button_click_numbers(8))
Btn_9 = Button(root, text="9", padx=35, pady=20, command=lambda: button_click_numbers(9))
Btn_0 = Button(root, text="0", padx=35, pady=20, command=lambda: button_click_numbers(0))

Btn_add = Button(root, text="+", padx=15, pady=10, command=button_click_add)
Btn_sub = Button(root, text="-", padx=15, pady=10, command=button_click_sub)
Btn_mul = Button(root, text="*", padx=15, pady=10, command=button_click_mul)
Btn_div = Button(root, text="/", padx=15, pady=10, command=button_click_div)

Btn_result = Button(root, text="=", padx=15, pady=10, command=button_click_result)
Btn_clear = Button(root, text="Clear", padx=35, pady=10, command=button_click_clear)


# Put it on the Screen
Btn_1.grid(row=3, column=0)
Btn_2.grid(row=3, column=1)
Btn_3.grid(row=3, column=2)

Btn_4.grid(row=2, column=0)
Btn_5.grid(row=2, column=1)
Btn_6.grid(row=2, column=2)

Btn_7.grid(row=1, column=0)
Btn_8.grid(row=1, column=1)
Btn_9.grid(row=1, column=2)

Btn_0.grid(row=4, column=0)

Btn_result.grid(row=4, column=2)
Btn_clear.grid(row=4, column=1)

Btn_add.grid(row=5, column=1)
Btn_sub.grid(row=5, column=2)
Btn_mul.grid(row=6, column=1)
Btn_div.grid(row=6, column=2)


# Start gui and loop over it to react on changes
root.mainloop()
