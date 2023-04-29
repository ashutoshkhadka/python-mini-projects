import turtle
import turtle as t
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Turtle Race", prompt="Which color turtle do you bet on?")
colors = ["blue", "red", "green", "yellow", "orange", "black"]
y_coor = [100, 60, 20, -20, -60, -100]
turtles = []

for color in colors:
    squirtle = t.Turtle(shape="turtle")
    squirtle.color(color)
    turtles.append(squirtle)

for i in range(0, 6):
    turtles[i].penup()
    turtles[i].goto(-230, y_coor[i])

game_not_over = True
while game_not_over:
    for turtle in turtles:
        dist = random.randint(0, 10)
        turtle.forward(dist)
        if turtle.xcor() >= 220:
            game_not_over = False
            print(f"Winner Winner Chicken Dinner 🍗: {turtle.color()} ")
            if user_bet == turtle.color():
                print("You win 🥳")
            else:
                print("Sorry, you lose 🤷‍")

screen.exitonclick()
