# Challenge: Modify the add function to take an unlimited number of arguments. Use a loop to sum
# all the arguments inside the function. Test it out by calling add() to calculate sum of arguments

# Solution
def add(*args):
    result = 0
    for num in args:
        result += num
    return result
print(f"Sum : {add(3, 3,9)}")

# **kwargs -> Many Keyword Argument
def calculation(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"Value of {key} is {value}")
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculation(5, add = 3, multiply =5)

# More Example for **kwargs

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seat = kwargs.get("seat")

my_car = Car(make="Ferrari")
print(my_car.model)
