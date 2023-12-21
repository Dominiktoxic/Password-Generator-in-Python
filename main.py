from tkinter import *
import random
import string
import pyperclip

# Functions
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    entry.delete(0, "end")
    entry.insert(0, password)

def clipcopy(text):
    pyperclip.copy(text)

# Constants
MAX_WIDTH = 500
MAX_HEIGHT = 300

# Initializing Window
app = Tk()
app.title("Password Generator")

title = Label(app, text="Password Generator", font=("Arial Black", 30))
title.pack()

length = Label(app, text="Length", font=("Arial Bold", 20))
length.pack()

scale = Scale(app, from_=0, to=30, orient="horizontal", length=350, tickinterval=30, font=("Arial Bold", 9))
scale.pack()

genPwd = Button(app, text="Generate Password", font=("Arial Bold", 10), command=lambda: generate_password(scale.get()))
genPwd.pack()

entry = Entry(app, font=("Arial Bold", 15))
entry.place(x=135, y=210)

copy = Button(app, text="Copy", font=("Arial Bold", 10), command= lambda: clipcopy(entry.get()))
copy.place(x=370, y=210)

app.maxsize(MAX_WIDTH, MAX_HEIGHT)
app.minsize(MAX_WIDTH, MAX_HEIGHT)

app.mainloop()