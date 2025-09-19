from tkinter import *

FONT = ("Times New Roman", 18, "normal")
KM = 1.609344

window = Tk()
window.title("Mile to KM converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

# Entry
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Label 1 - Miles
label = Label(text="Miles", font=FONT)
label.grid(column=2, row=0)

# Label 2 - is equal to
label2 = Label(text="is equal to", font=FONT)
label2.grid(column=0, row=1)

# Label 3 - Result
label3 = Label(text="0", font=FONT)
label3.grid(column=1, row=1)

# Label 4 - Unit - KM
label4 = Label(text="KM", font=FONT)
label4.grid(column=2, row=1)

# Button
def handle_on_calculate():
    user_input = entry.get()
    converted_result = float(user_input) * KM
    label3.config(text=converted_result)

button = Button(text="Calculate", command=handle_on_calculate)
button.grid(column=1, row=2)


window.mainloop()