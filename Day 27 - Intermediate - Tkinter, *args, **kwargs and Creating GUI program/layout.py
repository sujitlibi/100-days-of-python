from tkinter import *

from pandas.io.sas.sas_constants import column_label_length_length


def handle_on_btn_clicked():
    user_input = entry.get()
    label.config(text=user_input)

window = Tk()
window.title("Layout Example")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# Label
label = Label(text="This is Layout example", font=("Times New Roman", 18, "bold"))
# label.pack()
# label.place(x=100, y=100)
label.grid(column=0, row=0)
label.config(padx=2, pady=2)

# Button
button1 = Button(text="Click me", command=handle_on_btn_clicked)
button2 = Button(text="New Button")
button1.grid(column=1, row=1)
button2.grid(column=3, row=0)
# button.pack()

# Entry
entry = Entry(width=30)
entry.grid(column=4, row=3)
# entry.pack()





window.mainloop()