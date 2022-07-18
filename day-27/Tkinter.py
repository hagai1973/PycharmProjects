from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = my_input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=150, height=100)
window.config(padx=20, pady=20)

# Entry
my_input = Entry(width=10)
print(my_input.get())
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
my_label2 = Label(text="Km", font=("Arial", 10, "bold"))
my_label2.config(padx=5, pady=5)
my_label2.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# new_button = Button(text="New Button")
# # new_button.place(x=0, y=-100)
# new_button.grid(column=2, row=0)



# my_input.grid(column=3, row=2)

window.mainloop()
