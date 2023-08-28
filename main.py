import turtle
import pandas
from labels import Labels

data = pandas.read_csv("50_states.csv")
# Keep track of the score
correct = []

screen = turtle.Screen()
screen.title("Name All 50 US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Use a while loop to allow the user to keep guessing
while len(correct) < 50:
    # Convert the guess to title case for better matching experience
    answer = screen.textinput(title=f"{len(correct)}/50 States Correct", prompt="Name a State").title()

    if answer == "Exit":
        # Save states that the user needs to learn to csv
        states_to_learn = [state for state in data.state.to_list() if state not in correct]
        pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
        break

    # Check if the guess is among the states
    if answer in data.state.values:
        row = data[data.state == answer]
        # Write correct guesses onto the map
        Labels(answer, (int(row.x), int(row.y)))
        # Record the correct guesses in a list
        correct.append(answer)

else:
    turtle.clearscreen()
    image = "you_win.gif"
    screen.addshape(image)
    turtle.shape(image)


screen.mainloop()


