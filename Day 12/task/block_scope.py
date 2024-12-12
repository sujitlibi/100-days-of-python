# Python is a bit different from other programming
# languages in that it does not have block scope.
#
# This means that variables created nested in other
# blocks of code e.g. for loops, if statements, while loops etc.
# don't get local scope. They are given function scope
# if they are within a function or global scope if they are not.
#
# e.g.
# Accessible anywhere
# my_global_var = 1
#
# def my_function():
#     # Only accessible within my_function()
#     my_local_var = 2
#
# for _ in range(10):
#     # Accessible anywhere
#     my_block_var = 3

# There is no such thing like Block Scope in Python!!!!!!

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()
# print(new_enemy) // error