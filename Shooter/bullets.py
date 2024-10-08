from turtle import Turtle

class Bullets:
    def __init__(self, rocket):
        self.bullets = []
        self.rocket = rocket

    def shoot(self):
        bullet = Turtle()
        bullet.hideturtle()
        bullet.color("white")
        bullet.shape("circle")
        bullet.penup()
        bullet.goto(self.rocket.xcor(), self.rocket.ycor())
        bullet.setheading(90)
        self.bullets.append(bullet)

    def move_bullets(self):
        for bullet in self.bullets:
            bullet.showturtle()
            bullet.forward(20)
            if bullet.ycor() > 300:
                self.delete_bullet(bullet)

    def delete_bullet(self, bullet):
        bullet.hideturtle()
        self.bullets.remove(bullet)

    def update(self):
        self.move_bullets()
