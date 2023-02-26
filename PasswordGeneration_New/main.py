from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
# canvas.pack()
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=34)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=34)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1, columnspan=2)


# Buttons
genrate_password_button = Button(text='Generate Password', width=18)
genrate_password_button.grid(row=4, column=2, padx=1, pady=10)
add_button = Button(text='Add', width=18)
add_button.grid(row=4, column=1, columnspan=1, padx=1, pady=10)


window.mainloop()
