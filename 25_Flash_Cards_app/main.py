from tkinter import *

#--------------------- Constants -----------------------------#
BACKGROUND_COLOR = "#B1DDC6"


#--------------------- UI Setup -----------------------------#
window = Tk()
window.title("Flash Cards App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_image)
canvas.grid(row=0, column=0, columnspan=2)

language_label = Label(text="English", font=("Ariel", 40, "italic"))
language_label.place(x=300, y=150)

word_label = Label(text="Word", font=("Ariel", 60, "bold"))
word_label.place(x=300, y=200)
word_label.place(x=300, y=263)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
correct_button = Button(image=right_image, highlightthickness=0)
correct_button.grid(row=1, column=1)

window.mainloop()