from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.gotostart()
        self.setheading(90)
    def goup(self):
        self.forward(MOVE_DISTANCE)
    def gotostart(self):
        self.goto(STARTING_POSITION)
    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True 
        else:
            return False



