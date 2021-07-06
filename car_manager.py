from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.allcars =[]
        self.carspeed =STARTING_MOVE_DISTANCE
    def createcars(self):
        if random.randint(1,6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y =random.randint(-250,250)
            new_car.goto(300,y)
            self.allcars.append(new_car)
    def move(self):
        for cars in self.allcars:
            cars.backward(self.carspeed)
    def level(self):
        self.carspeed+= MOVE_INCREMENT


