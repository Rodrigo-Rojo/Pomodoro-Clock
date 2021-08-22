from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def time_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global checkmark
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        countdown(work_time)
        timer_label.config(text="Work")
    elif reps == 1 or 3 or 5:
        countdown(short_break_time)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(long_break_time)
        timer_label.config(text="Break", fg=RED)
    if reps == 2:
        checkmark = "✔"
    elif reps == 4:
        checkmark = "✔✔"
    elif reps == 6:
        checkmark = "✔✔✔"
    checkmark_label.config(text=checkmark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        reps += 1
        if reps < 8:
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

checkmark_label = Label(text=checkmark, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(column=1, row=4)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=3)
reset_button = Button(text="Reset", command=time_reset)
reset_button.grid(column=2, row=3)

window.mainloop()
