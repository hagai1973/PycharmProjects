from tkinter import *
import math
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
LONG_BREAK_MIN = 2
SHORT_BREAK_MIN = 1
REPS = 0
CM = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="", fg=GREEN, font=(FONT_NAME, 12, "bold"), bg=YELLOW)
    title_label.config(text="Timer", fg=RED, font=(FONT_NAME, 45, "bold"), bg=YELLOW)
    global REPS
    global CM
    REPS = 0
    CM = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    global CM
    cm_str = ""
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    i = 0
    while i < CM:
        cm_str += "✔"
        i += 1
    check_marks.config(text=cm_str, fg=GREEN, font=(FONT_NAME, 12, "bold"), bg=YELLOW)

    if REPS % 2 == 0 and REPS < 8:
        count_down(short_break_sec)
        title_label.config(text="Break(s)", fg=PINK, font=(FONT_NAME, 45, "bold"), bg=YELLOW)
    elif REPS % 2 != 0:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 45, "bold"), bg=YELLOW)
        CM += 1


    else:
        count_down(long_break_sec)
        title_label.config(text="Break(l)", fg=RED, font=(FONT_NAME, 45, "bold"), bg=YELLOW)

    if REPS > 8:
        REPS = 0






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = str(int((count / 60)))
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(100, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)
# title_label.pack()


canvas = Canvas(width=250, height=266, bg=YELLOW, highlightthickness=0)

tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(130, 155, image=tomato_image)
timer_text = canvas.create_text(130, 155, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# count_down(5)
canvas.grid(column=1, row=1)

title_start = Button(text="Start", fg="#31087B", font=(FONT_NAME, 12, "bold"), bg=YELLOW, highlightthickness=0,
                     command=start_timer)
title_start.grid(column=0, row=2)

button_Reset = Button(text="Reset", fg="#31087B", font=(FONT_NAME, 12, "bold"), bg=YELLOW, highlightthickness=0,
                      command=reset_timer)
button_Reset.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, font=(FONT_NAME, 12, "bold"), bg=YELLOW)
check_marks.grid(column=1, row=3)

# Keep window open
window.mainloop()