import pandas

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
import time

current_card ={}
word ={}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word = original_data.to_dict(orient="records")
else:
    word = data.to_dict(orient="records")


def next_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(can_img,image=image)
    flip_timer = window.after(3000,flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fil="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(can_img,image=english_image)

def is_known():
    word.remove(current_card)
    data = pandas.DataFrame(word)
    data.to_csv("data/words_to_learn.csv",index=False)


    next_word()

window = Tk()
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)

canvas = Canvas(height=526,width=800)
image = PhotoImage(file="images/card_front.png")
english_image = PhotoImage(file="images/card_back.png")

#To change the image:
#image2 = PhotoImage(file="images/card_back.png")
#canvas.create_image(400,263,image=image2)
can_img = canvas.create_image(400,263,image=image)

card_title = canvas.create_text(400,160,text="",font=('Arial',48,"italic"))
card_word = canvas.create_text(400,263,text="",font=('Arial',60,'bold'))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


# time.sleep(1)

flip_timer = window.after(3000,flip_card)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img,highlightthickness=0,command=is_known)
right_button.grid(row = 1,column=1)
left_img = PhotoImage(file="images/wrong.png")
left_button = Button(image=left_img,highlightthickness=0,command=next_word)
left_button.grid(row=1,column=0)
next_word()

window.mainloop()