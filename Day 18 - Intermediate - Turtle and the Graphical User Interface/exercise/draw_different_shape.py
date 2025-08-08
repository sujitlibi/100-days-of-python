from turtle import Turtle, Screen
import random

tim = Turtle()

def draw_shape(num_sides_of_shape):
    angle = 360 / num_sides_of_shape
    for _ in range(num_sides_of_shape):
        tim.forward(100)
        tim.right(angle)

for side_of_shape in range(3, 10):
    tim.color(random.random(), random.random(), random.random()) # or we can list down array of color and select randomly for it
    draw_shape(side_of_shape)

screen = Screen()
screen.exitonclick()