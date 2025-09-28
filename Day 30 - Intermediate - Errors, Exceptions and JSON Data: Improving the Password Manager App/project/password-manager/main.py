from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip, json

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

# ---------------------------- SEARCH WEBSITE ------------------------------ #
def search_info():
    try:
        with open("password.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="Information no available")
    else:
        title = website_entry.get()
        try:
            fetch_data = data[title]
            messagebox.askokcancel(title=title, message=f"email: {fetch_data["email"]} \n password: {fetch_data["password"]}")
        except KeyError:
            messagebox.showinfo(title="Oops", message="Information no available")

    # Angela solution
    # website = website_entry.get()
    # try:
    #     with open("data.json") as data_file:
    #         data = json.load(data_file)
    # except FileNotFoundError:
    #     messagebox.showinfo(title="Error", message="No Data File Found.")
    # else:
    #     if website in data:
    #         email = data[website]["email"]
    #         password = data[website]["password"]
    #         messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    #     else:
    #         messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_entry = {
        website : {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please don't leave any field empty.")
    else:
        try:
            with open("password.json", mode="r") as file:
                # Load Data
                data = json.load(file)
        except FileNotFoundError:
            with open("password.json", mode="w") as file:
                json.dump(new_entry, file, indent=4)
        else:
            # update old data with new data
            data.update(new_entry)
            with open("password.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
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

website_entry = Entry(width=21, fg="black", bg="white", highlightthickness=0)
website_entry.grid(column=2, row=3)
website_entry.focus()

# Search Component
search_btn = Button(text="Search", width=13, fg="black", bg="white", highlightthickness=0, command=search_info)
search_btn.grid(column=3, row=3)

# Email / Username Component
email_label = Label(text="Email/Username:", fg="black", bg="white", font=NORMAL_FONT)
email_label.grid(column=1, row=4)

email_entry = Entry(width=35, fg="black", bg="white", highlightthickness=0)
email_entry.grid(column=2, row=4, columnspan=3)

# Password Component
password_label = Label(text="Password:", fg="black", bg="white", font=NORMAL_FONT)
password_label.grid(column=1, row=5)

password_entry = Entry(width=21, fg="black", bg="white", highlightthickness=0)
password_entry.grid(column=2, row=5)

generate_password_btn = Button(text="Generate Password", fg="black", bg="white", highlightthickness=0, bd=0, command=generate_password)
generate_password_btn.grid(column=3, row=5)

# Add Button Component
add_info_btn = Button(text="Add", width=35, fg="black", bg="white", highlightthickness=0, bd=0, command=save_password)
add_info_btn.grid(column=2, row=6, columnspan=3)


window.mainloop()