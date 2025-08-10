from turtle import Turtle

STARTING_POSITIONS =   [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20

class Snake:
    def __init__(self):
        self.body_segments = []
        self.create_snake()

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
        self.body_segments[0].fd(MOVING_DISTANCE)