from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

NORMAL_FONT = ("Times New Roman", 18, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please don't leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("password.text", mode="a") as file:
                file.write(f"\n{website} | {email} | {password}")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Title Label
# title_label = Label(text="Password Manager", fg="black", bg="white", font=("Times New Roman", 32, "bold"))
# title_label.grid(column=2, row=1)

# Canvas setup
canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=2, row=2)

# Website Component
website_label = Label(text="Website:", fg="black", bg="white", font=NORMAL_FONT)
website_label.grid(column=1, row=3)

website_entry = Entry(width=35, fg="black", bg="white", highlightthickness=0)
website_entry.grid(column=2, row=3, columnspan=2)
website_entry.focus()

# Email / Username Component
email_label =Label(text="Email/Username:", fg="black", bg="white", font=NORMAL_FONT)
email_label.grid(column=1, row=4)

email_entry = Entry(width=35, fg="black", bg="white", highlightthickness=0)
email_entry.grid(column=2, row=4, columnspan=2)

# Password Component
password_label = Label(text="Password:", fg="black", bg="white", font=NORMAL_FONT)
password_label.grid(column=1, row=5)

password_entry = Entry(width=21, fg="black", bg="white", highlightthickness=0)
password_entry.grid(column=2, row=5)

generate_password_btn = Button(text="Generate Password", fg="black", bg="white", highlightthickness=0, bd=0, command=generate_password)
generate_password_btn.grid(column=3, row=5)

# Add Button Component
add_info_btn = Button(text="Add", width=35, fg="black", bg="white", highlightthickness=0, bd=0, command=save_password)
add_info_btn.grid(column=2, row=6, columnspan=2)


window.mainloop()