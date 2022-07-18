from tkinter import *


def button_click(**ky):
    # print("clicked me...")
    # my_label.config(text=my_input.get())
    km = km_input.get()
    my_label.config(text="to km: " + str(int(km) * 1.8))


#
# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
#
# # print(add(5,6,9,10, 22))
#
# def calculate(n, **kwargs):
#     # print(kwargs)
#     result = 0
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#         n += int(kwargs["add"])
#         n *= int(kwargs["multply"])
#         return n

#
# print(calculate(2, add=3, multply=5))

# Create tkindter window

'''
Create tkinter window settings 
'''

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

'''
Create label
'''

my_label = Label(text="My label", font=("Arial", 20, "bold"))
my_label.pack()

# Update exit object

my_label["text"] = "new Text"
my_label.config(text="new text")

my_button = Button(text="Click me to convert", font=("Arial", 8, "bold"), command=button_click)
my_button.pack()

km_input = Entry(width=20)
km_input.insert(END, string="Type km to convert")
km_input.pack()

text = Text(width=30, height=5)
text.focus
text.insert(END, "multi line txt entry")
print(text.get("1.0", END))
text.pack()


def spin_used():
    print(spin.get())


spin = Spinbox(from_=1, to=5, width=5, command=spin_used)
spin.pack()


def scale_use(value):
    print(value)


scale = Scale(from_=1, to=10, command=scale_use)
scale.pack()


def cb_used():
    print(checked_state.get())


checked_state = IntVar()
cb = Checkbutton(text="Turn on / of", variable=checked_state, command=cb_used)
checked_state.get()
cb.pack()


def rb_used():
    print(rb_state.get())


rb_state = IntVar()
rb1 = Radiobutton(text="Option A", value=1, variable=rb_state, command=rb_used)
rb2 = Radiobutton(text="Option B", value=2, variable=rb_state, command=rb_used)
rb1.pack()
rb2.pack()


def listbox_used(event):
    print(my_list.get(my_list.curselection()))


my_list = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange"]

for item in fruits:
    my_list.insert(fruits.index(item), item)

my_list.bind("<<ListboxSelect>>", listbox_used)
my_list.pack()

window.mainloop()

