from turtle import Turtle

class Rocket(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("blue")
        self.penup()
        self.goto(0, -250)
        self.left(90)
