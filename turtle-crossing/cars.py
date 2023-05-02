import random
from turtle import Turtle

CAR_SPEED = 5
SPEED_INCR = 2
COLORS = ["red", "yellow", "blue", "purple", "black", "orange", "green"]


class Cars():
    def __init__(self):
        self.cars = []
        self.car_speed = CAR_SPEED

    def generate(self):
        if random.randint(1, 6) == 5:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.shapesize(stretch_len=2)
            car.goto(310, random.randint(-250, 250))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += SPEED_INCR
