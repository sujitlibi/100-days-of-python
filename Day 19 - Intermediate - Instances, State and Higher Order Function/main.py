from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(30)

screen.listen()

screen.onkey(move_forward, "space")

screen.exitonclick()