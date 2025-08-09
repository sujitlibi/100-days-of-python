# from turtle import Turtle, Screen
#
# screen = Screen()
# screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
# colors = ["red", "orange", "yellow", "green", "blue", "purple", "indigo"]
# current_x_axis = -230
# current_y_axis = -100
#
# for turtle_color in colors:
#     tim = Turtle(shape="turtle")
#     tim.color(turtle_color)
#     tim.penup()
#     tim.goto(x=current_x_axis, y=current_y_axis)
#     # current_x_axis = current_x_axis + 10
#     current_y_axis = current_y_axis + 25
#
#
# screen.exitonclick()

import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "indigo"]
y_position = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []

for turtle_index in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()