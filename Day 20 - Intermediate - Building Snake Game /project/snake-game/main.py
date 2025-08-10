from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position =[(0,0), (-20,0), (-40,0)]

for position in starting_position:
    snake_body_segment = Turtle(shape="square")
    snake_body_segment.color("white")
    snake_body_segment.goto(position)

screen.exitonclick()