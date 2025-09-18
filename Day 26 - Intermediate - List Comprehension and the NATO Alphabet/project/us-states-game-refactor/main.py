# Solution By Angela Yu
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./assets/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./data/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./score/states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        # or data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        # t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()



# My Solution
# import turtle
# import pandas
# from scoreboard import Scoreboard
#
# screen = turtle.Screen()
# screen.title("US States Game")
# image = "./assets/blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
# data = pandas.read_csv("./data/50_states.csv")
#
# is_game_on = True
#
# writer = turtle.Turtle()
# writer.color("black")
# writer.penup()
# writer.hideturtle()
#
# scoreboard = Scoreboard()
#
# def ask_to_guess():
#     return screen.textinput(title=f"{scoreboard.score}/50 States Correct", prompt="What's another state's name?").title()
#
# while is_game_on:
#     screen.update()
#     answer_state = ask_to_guess()
#     correct_guesses = []
#     fetched_state = data[data["state"] == answer_state]
#     if len(fetched_state):
#         correct_guesses.append(answer_state)
#         scoreboard.increase_score()
#         state_x = int(fetched_state["x"].iloc[0])
#         state_y = int(fetched_state["y"].iloc[0])
#
#         writer.goto(state_x, state_y)
#         writer.write(f"{answer_state}", align="center", font=("Courier", 12, "normal"))


