from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(height=600, width=800)
screen.title("Turtle Crossing Road")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")


is_game_on = True

while is_game_on:
    time.sleep(car_manager.move_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Detect if turtle crossed the road
    if player.ycor() > 280:
        player.reset_turtle_position()
        scoreboard.increase_score()

    # Detect turtle collision with car
    for each_car in car_manager.all_generated_cars[1:]:
        if each_car.distance(player) < 20:
            is_game_on =False
            scoreboard.game_over()


screen.exitonclick()