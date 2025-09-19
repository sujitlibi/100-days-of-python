from tkinter import *

window = Tk()
window.title("Challenge 2")
window.minsize(width=500, height=500)

# Label
my_label = Label(text="User Entered Data will show up here", font=("Times New Roman", 24, "bold"))
my_label.pack()

# Entry
user_input = Entry(width=20)
user_input.pack()

# Button
def handle_on_submit():
    my_label.config(text=f"{user_input.get()}")

my_button = Button(text="Submit", command=handle_on_submit)
my_button.pack()


window.mainloop()