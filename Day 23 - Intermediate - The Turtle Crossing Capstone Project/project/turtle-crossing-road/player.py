from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        # print(self.xcor(), self.ycor())
        # new_turtle_position = self.ycor() + 10
        # self.goto(0, new_turtle_position)
        self.forward(10)

    def reset_turtle_position(self):
        self.goto(0, -280)