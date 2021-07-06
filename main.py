import time
from turtle import Screen
from player import Player
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager =CarManager()

screen.listen()
screen.onkey(player.goup,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.createcars()
    car_manager.move()
    for cars in car_manager.allcars:
        if cars.distance(player)<20:
            game_is_on = False
    if player.finish():
        player.gotostart()
        car_manager.level()

screen.exitonclick()
