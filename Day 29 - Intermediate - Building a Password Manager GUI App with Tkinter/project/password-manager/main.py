from tkinter import *

NORMAL_FONT = ("Times New Roman", 18, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

generate_password_btn = Button(text="Generate Password", fg="black", bg="white", highlightthickness=0, bd=0)
generate_password_btn.grid(column=3, row=5)

# Add Button Component
add_info_btn = Button(text="Add", width=35, fg="black", bg="white", highlightthickness=0, bd=0)
add_info_btn.grid(column=2, row=6, columnspan=2)


window.mainloop()