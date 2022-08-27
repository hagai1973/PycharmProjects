from tkinter import *


def button_clicked():
    # print("I got clicked")
    new_text = my_input.get()
    if radio_state.get() == 1:
        to_km = round(float(new_text) * 1.609, 2)
        my_label3.config(text=to_km)
    else:
        to_miles = round(float(new_text) / 1.609, 2)
        my_label3.config(text=to_miles)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=150, height=100)
window.config(padx=20, pady=20)

# Entry
my_input = Entry(width=10)
# print(my_input.get())
my_input.grid(column=1, row=0)

# Label
my_label = Label(text="Miles", font=("Arial", 10, "bold"))
# my_label.config(text="Miles")
my_label.config(padx=5, pady=5)
my_label.grid(column=2, row=0)

# Label
my_label2 = Label(text="is equal to", font=("Arial", 10, "bold"))
my_label2.config(padx=5, pady=5)
my_label2.grid(column=0, row=1)

# Label
my_label3 = Label(text="0", font=("Arial", 10, "bold"))
my_label3.config(padx=5, pady=5)
my_label3.grid(column=1, row=1)

# Label
my_label4 = Label(text="Km", font=("Arial", 10, "bold"))
my_label4.config(padx=5, pady=5)
my_label4.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


def radio_used():
    if radio_state.get() == 1:
        my_label4.config(text="Km")
        my_label.config(text="Miles")
    else:
        my_label4.config(text="Miles")
        my_label.config(text="Km")

    # print(radio_state.get())

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Miles to Km", value=1, variable=radio_state, command=radio_used)
radiobutton1.select()
radiobutton2 = Radiobutton(text="Km to Miles", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=1, row=3)
radiobutton2.grid(column=2, row=3)
# new_button = Button(text="New Button")
# # new_button.place(x=0, y=-100)
# new_button.grid(column=2, row=0)


# my_input.grid(column=3, row=2)

window.mainloop()
