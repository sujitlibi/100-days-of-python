import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "./assets/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("./data/50_states.csv")

is_game_on = True

writer = turtle.Turtle()
writer.color("black")
writer.penup()
writer.hideturtle()


def ask_to_guess():
    return screen.textinput(title="Guess Next State", prompt="What's another state's name?").title()

while is_game_on:
    screen.update()
    answer_state = ask_to_guess()
    fetched_state = data[data["state"] == answer_state]
    if len(fetched_state):
        state_x = int(fetched_state["x"].iloc[0])
        state_y = int(fetched_state["y"].iloc[0])

        writer.goto(state_x, state_y)
        writer.write(f"{answer_state}", align="center", font=("Courier", 12, "normal"))

# def get_mouse_click_cord(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cord)
# turtle.mainloop()
# screen.exitonclick()