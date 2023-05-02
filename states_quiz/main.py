import turtle as t
import pandas as pd

df = pd.read_csv("50_states.csv")

screen = t.Screen()
screen.title("U.S. States Quiz")
img = "blank_states_img.gif"
screen.addshape(img)
t.shape(img)

guessed_states = []


def create_label():
    global text
    text = t.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(x, y)
    text.write(ans, font=("Arial", 12, "normal"))

def create_report():
    missed_states = []
    for state in df.state:
        if state not in guessed_states:
            missed_states.append(state)
    missed_data = pd.DataFrame(missed_states)
    missed_data.to_csv("report.csv")

manual_override = False
while len(guessed_states) < 50 and not manual_override:
    ans = screen.textinput(title=f"Guess the State. ({len(guessed_states)}/50 Correct)", prompt="Name a state").title()
    if ans in set(df.state):
        df_state = df[df.state == ans]
        x = df_state.x.item()
        y = df_state.y.item()
        create_label()
        guessed_states.append(ans)
    elif ans == "Exit":
        manual_override = True
        create_report()

screen.exitonclick()
