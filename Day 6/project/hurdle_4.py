# My Solution:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_right()
#     move()
#     turn_right()
#     move()
#
# while not at_goal():
#     if not wall_in_front() or front_is_clear():
#         move()
#     if not is_facing_north() and wall_in_front():
#         turn_left()
#     if not wall_in_front() or front_is_clear():
#         move()
#     if is_facing_north() and right_is_clear():
#         jump()


# Angela Solution:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
