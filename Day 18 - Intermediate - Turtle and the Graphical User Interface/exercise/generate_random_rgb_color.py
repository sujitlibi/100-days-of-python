from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

screen.colormode(255)
tim.shape("turtle")
tim.pensize(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]

for _ in range(200):
    tim.pencolor(random_color())
    tim.setheading(random.choice(direction))
    tim.forward(50)

screen.exitonclick()