# Name All 50 US States Game

## **[100 Days of Code: The Complete Python Pro Bootcamp for 2023](https://www.udemy.com/course/100-days-of-code/)**

By Dr. Angela Yu

*Day 25 of 100:* Working with CSV Data and the Pandas Library

## Project Specs

Using **[Turtle](https://docs.python.org/3/library/turtle.html)** and the **[Pandas Data Analysis](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)** library, program a game where a user attempts to name all 50 US states.

This application is written with Python 3.11.

![US States Game Preview](https://github-readme.s3.us-west-1.amazonaws.com/USStatesGame.png)

### Main Features
To play the game, a user is presented with a map of the United States and an input prompt that shows the current count of state names that have been guessed correctly.

As the user correctly guesses a state name, the name appears on the map within the shape of that particular state.

If the user cannot remember any additional state names, they can type 'exit' into the prompt to download a "States to Learn" CSV.

## Usage & Requirements

This project uses two libraries:
- Turtle
- Pandas

and one class:
- Label

### Workflow
State names and map coordinates are stored in a `.csv` file and read into Python using the Pandas library. 

Using the Pandas `.read_csv` functionality, we read in the data for the game:
```
data = pandas.read_csv("50_states.csv")
```

We then create the Graphic User Interface (GUI) using the `turtle.Screen()` function, set the game title, and load the map of the United States:  

```angular2html
screen = turtle.Screen()
screen.title("Name All 50 US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
```

Once the map is drawn, we prompt the user to Name a State and start the game:

![US States Game User Prompt](https://github-readme.s3.us-west-1.amazonaws.com/USStatesGame-prompt.png)

The game continues until the user either guesses all 50 states correctly, or types `exit` into the prompt.

If the user guesses all 50 states correctly, they are presented with a celebration image:

```angular2html
turtle.clearscreen()
image = "you_win.gif"
screen.addshape(image)
turtle.shape(image)
```

![US States Game Winner Graphic](https://github-readme.s3.us-west-1.amazonaws.com/USStatesGame-win.png)

If the user reaches a point where they can no longer remember any state names, they then type `exit` into the prompt and the application will create a "States to Learn" `.csv` file, listing all of the states the user did not enter.

# Getting Started

All of the commands below should be typed into the Python terminal of your IDE (I use PyCharm for my Python Development).

First, clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:shelbyblanton/us-states-game.git
    
Then open the project in PyCharm.
    
In the `main.py` file, click on the word `pandas` in the import statement at the top of the page. Then click on the red exclamation point and click `Install Package Pandas` to load the library:

![Install Pandas Library Example](https://github-readme.s3.us-west-1.amazonaws.com/Install-Pandas.png)

**Setup is complete!** 

Click Run in PyCharm to see the app in action.


# Author & Credits

Programmed by **[M. Shelby Blanton](https://www.linkedin.com/in/shelbyblanton/)** under the instructional guidance of **[Dr. Angela Yu](https://www.udemy.com/user/4b4368a3-b5c8-4529-aa65-2056ec31f37e/)** via **[Udemy.com](udemy.com)**.
