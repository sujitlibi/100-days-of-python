from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(10)

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random.choice(colours))
    tim.setheading(random.choice(direction))
    tim.forward(50)

screen = Screen()
screen.exitonclick()