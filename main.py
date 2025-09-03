import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

correct_answer = []
wrong_answer = []
lives = 3

while len(correct_answer) <50 and lives> 0:
    answer_state = screen.textinput(title=f"{len(correct_answer)}/50 states, Lives: {lives}",
                                    prompt="Type a state name: ").title()

    if answer_state == "Exit":
        break

    if answer_state in states_list and answer_state not in correct_answer:

        correct_answer.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state ==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)

    else:

        if answer_state not in wrong_answer:
            wrong_answer.append(answer_state)
            lives -= 1

        if lives == 0:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(0,0)
            t.write("Game Over", align="center", font=("Courier", 20, "normal"))

# ---------------- SAVE MISSED STATES ---------------- #
states_to_learn = [state for state in states_list if state not in correct_answer]
df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")






    

