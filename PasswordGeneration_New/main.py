from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == '' or password == '':
        is_valid = False
        messagebox.showinfo(title="Error", message="Do not leave empty entries...")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"following details were entered: \n email: {email} \n password: {password}")
        if is_ok:
            website_entry.delete(0, END)
            # email_entry.delete(0, END)
            password_entry.delete(0, END)

            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
# canvas.pack()
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky=W)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0, sticky=W)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, sticky=W)

# Entries
website_entry = Entry(width=34)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W, padx=10)
website_entry.focus()
email_entry = Entry(width=34)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W, padx=10)
email_entry.insert(0, 'hagai1973@gmail.com')
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1, columnspan=2, sticky=W, padx=10)

# Buttons
genrate_password_button = Button(text='G', width=2, padx=10)
genrate_password_button.grid(row=3, column=2, sticky=W)
add_button = Button(text='Add', width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2, padx=1, pady=10)

window.mainloop()
