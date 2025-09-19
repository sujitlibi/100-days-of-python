# if we import tkinter like below:
# from tkinter import *
# we can use like this
# window = Tk()
# my_label = Label(...args)


import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am just a Label", font=("Ariel", 24, "bold"))
my_label.pack()

# For single attribute update
# my_label["text"] = "Just got updated"

# For updating multiple attributes
my_label.config(text="This is third time i got updated", font=("Times New Roman", 18, "bold"))

# Button
def handle_button_click():
    print("I just got clicked!!!!")
    # my_label.config(text="Button Got Clicked!!")
    my_label.config(text=f"{user_input.get()}")

my_button = tkinter.Button(text="Click me!", command=handle_button_click)
my_button.pack()

# Entry
user_input = tkinter.Entry(width=20)
user_input.pack()



window.mainloop()