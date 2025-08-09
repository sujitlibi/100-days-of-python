from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def rotate_clockwise():
    # tim.right(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def rotate_anti_clockwise():
    # tim.left(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_backward, "s")
screen.onkey(move_forward, "w")
screen.onkey(rotate_clockwise, "d")
screen.onkey(rotate_anti_clockwise, "a")
screen.onkey(clear, "c")
screen.exitonclick()