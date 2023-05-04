import random
from tkinter import *
import pandas as pd

GREEN = "#B1DDC6"

try:
    df = pd.read_csv("data/rem_data.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")

learn_dictionary = df.to_dict(orient="records")
random_entry = {}


def remove_and_save_entry():
    learn_dictionary.remove(random_entry)
    leftover_words = pd.DataFrame(learn_dictionary)
    leftover_words.to_csv("data/rem_data.csv", index=False)
    pick_random_word()


def pick_random_word():
    print(len(learn_dictionary))
    global random_entry, flip_timer
    window.after_cancel(flip_timer)
    random_entry = random.choice(learn_dictionary)
    canvas.itemconfig(card_image, image=front_card)
    canvas.itemconfig(lang_canvas, text="French", fill="black")
    canvas.itemconfig(translation_canvas, text=random_entry["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=back_card)
    canvas.itemconfig(lang_canvas, text="English", fill="white")
    canvas.itemconfig(translation_canvas, text=random_entry["English"], fill="white")


window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=GREEN)

flip_timer = window.after(3000, func=flip_card)

front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
card_image = canvas.create_image(400, 265, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)

lang_canvas = canvas.create_text(400, 150, text="French", fill="black", font=('Arial', 40, 'italic'))
translation_canvas = canvas.create_text(400, 263, text="trouve", fill="black", font=('Arial', 60, 'bold'))

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, highlightbackground=GREEN, command=remove_and_save_entry)
tick_button.grid(row=1, column=0)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightbackground=GREEN, command=pick_random_word)
cross_button.grid(row=1, column=1)

pick_random_word()

window.mainloop()
