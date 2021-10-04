# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=5262s

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
from tkinter import filedialog
import sqlite3

# # Create a database and connect to it
# conn = sqlite3.connect("data/address_book.db")
#
# # Create a cursor
# c = conn.cursor()

# Create table - only needed once
# c.execute("""CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
#     )""")


root = Tk()
root.title("Address Database")
root.iconbitmap('./data/icon.ico')
# root.geometry("400x400")


def submit():
    # Create a database and connect to it
    conn = sqlite3.connect("data/address_book.db")

    # Create a cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :last_name, :address, :city, :state, :zipcode)",
              {
                  "f_name": f_name.get(),
                  "last_name": l_name.get(),
                  "address": address.get(),
                  "city": city.get(),
                  "state": state.get(),
                  "zipcode": zipcode.get()
              }
              )

    # Commit Changes to Database
    conn.commit()

    # Close Database Connection
    conn.close()

    # Clear Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    # Create a database and connect to it
    conn = sqlite3.connect("data/address_book.db")

    # Create a cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # c.fetchone()  # Returns first match
    # c.fetchmany(50)  # Return first 50 matches
    # print(records)

    print_record = ""
    for record in records:
        print_record += str(record) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=8, column=0, columnspan=2)


    # Commit Changes to Database
    conn.commit()

    # Close Database Connection
    conn.close()


# Create Entry Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# Create Entry Labels beside
f_name_label = Label(root, text="First Name: ")
f_name_label.grid(row=0, column=0, padx=20)
l_name_label = Label(root, text="Last Name: ")
l_name_label.grid(row=1, column=0, padx=20)
address_label = Label(root, text="Address: ")
address_label.grid(row=2, column=0, padx=20)
city_label = Label(root, text="City: ")
city_label.grid(row=3, column=0, padx=20)
state_label = Label(root, text="State: ")
state_label.grid(row=4, column=0, padx=20)
zipcode_label = Label(root, text="Zip Code: ")
zipcode_label.grid(row=5, column=0, padx=20)

# Create submit button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Start gui and loop over it to react on changes
root.mainloop()
