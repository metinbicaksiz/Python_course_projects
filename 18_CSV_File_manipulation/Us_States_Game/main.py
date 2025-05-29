from turtle import Turtle, Screen
from pandas import read_csv

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=720, height=480)

turtle = Turtle()
turtle.shape(image)

correct_guesses = 0

data = read_csv("50_states.csv")
all_states = data.state.to_list()

while correct_guesses < 50:
    answer_state = screen.textinput(title=f"{correct_guesses}/50 Guess the state",
                                    prompt="What's another state's name?").title()

    if answer_state in all_states:
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        correct_guesses += 1


screen.exitonclick()