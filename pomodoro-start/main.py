# ---------------------------- CONSTANTS ------------------------------- #
import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def start_timer():
    global reps
    work_secs = 25 * 60
    short_break_secs = 5 * 60
    long_break_secs = 20 * 60
    reps += 1
    if reps % 2 != 0:
        count_down(work_secs)
        title_label.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(long_break_secs)
        title_label.config(text="Break", fg=RED)
    elif reps > 8:
        pass
    else:
        count_down(short_break_secs)
        title_label.config(text="Break", fg=PINK)


def count_down(count):
    mins = math.floor(count / 60)
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"
    if count > -1:
        canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if (reps - 1) % 2 == 0:
            checkmark_label.config(text=checkmark_label.cget("text") + "✓")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 60, 'bold'), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start_btn = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(row=2, column=2)

checkmark_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
checkmark_label.grid(row=3, column=1)

window.mainloop()
