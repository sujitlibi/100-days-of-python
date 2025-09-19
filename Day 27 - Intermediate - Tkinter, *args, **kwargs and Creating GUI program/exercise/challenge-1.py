# Instruction
# Show "Button Got Clicked" on my_label when the button got clicked

from tkinter import *

window = Tk()
window.title("Challenge 1")
window.minsize(width=500, height=500)

# Let define first Label that we need to update after button clicked
my_label = Label(text="Hello Fellows!!!", font=("Times New Roman", 24, "bold"))
my_label.pack()

# Method to update Label
def handle_button_click():
    my_label.config(text="Button Just Clicked")

# Let create button here
my_button = Button(text="Click Me", command=handle_button_click)
my_button.pack()

window.mainloop()