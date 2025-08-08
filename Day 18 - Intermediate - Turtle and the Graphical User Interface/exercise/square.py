from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.color("blue")

for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen.exitonclick()