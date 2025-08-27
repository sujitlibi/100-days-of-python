from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):

        self.all_generated_cars = []
        self.create_car()
        self.move_speed = 0.1

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=4)
            new_car.penup()
            y_position = random.randint(-250, 250)
            new_car.goto(400, y_position)
            self.all_generated_cars.append(new_car)


    def move_car(self):
        for car in self.all_generated_cars:
            car.backward(STARTING_MOVE_DISTANCE)
    #
    # def generate_random_car(self):
    #     # x_position = random.randint(-395, 395)
