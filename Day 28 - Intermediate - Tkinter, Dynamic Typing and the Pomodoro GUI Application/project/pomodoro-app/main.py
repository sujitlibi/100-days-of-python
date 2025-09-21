import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_count_down():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label "Timer"
    timer_label.config(text="Timer")
    # reset check mark
    checkmark_label.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count_down():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif REPS % 2 == 0:
        # count_down(5 * 60) # 5 min => 300 seconds
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Timer",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global REPS
    count_in_min = math.floor(count / 60)
    count_in_second = count % 60

    if count_in_second < 10:
        count_in_second = f"0{count_in_second}"

    canvas.itemconfig(timer_text, text=f"{count_in_min}:{count_in_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count_down()
        marks = "" # ✓
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO APP")
# window.minsize(width=500, height=500)
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
timer_label.grid(column=2, row=1)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = background_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Start Button
start_btn = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_count_down)
start_btn.grid(column=1, row=3)

# Checkmark Label
checkmark_label = Label(text="", fg=GREEN, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
checkmark_label.grid(column=2, row=4)

# Reset Button
reset_btn = Button(text="Reset", highlightthickness=0, command=reset_count_down)
reset_btn.grid(column=3, row=3)


window.mainloop()