from turtle import Turtle

STARTING_POSITIONS =   [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.body_segments = []
        self.create_snake()
        self.snake_head = self.body_segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_body_segment = Turtle(shape="square")
            snake_body_segment.color("white")
            snake_body_segment.penup()
            snake_body_segment.goto(position)
            self.body_segments.append(snake_body_segment)

    def move(self):
        for seg_num in range(len(self.body_segments) - 1, 0, -1):
            new_x = self.body_segments[seg_num - 1].xcor()
            new_y = self.body_segments[seg_num - 1].ycor()
            self.body_segments[seg_num].goto(new_x, new_y)
        self.snake_head.fd(MOVING_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() !=LEFT:
            self.snake_head.setheading(0)
