from turtle import Turtle
FONT = ("Arial", 12, "normal")


class Labels(Turtle):

    def __init__(self, state, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(f"{state}", align="center", font=FONT)
