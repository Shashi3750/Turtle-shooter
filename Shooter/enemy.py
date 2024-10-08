from turtle import Turtle

class Enemy:
    def __init__(self, num_enemies):
        self.enemies = []
        self.create_enemies(num_enemies)

    def create_enemies(self, num_enemies):
        start_y = 250  # Starting y-position for all enemies
        for i in range(num_enemies):
            enemy = Turtle()
            enemy.shape("turtle")
            enemy.color("red")
            enemy.penup()
            enemy.speed(0)  
            enemy.right(90)
            # Set initial position with more variety on x-axis for each enemy
            start_x = -250 + (i * 80)
            enemy.goto(start_x, start_y)
            self.enemies.append(enemy)

    def move(self):
        for enemy in self.enemies:
            # Extremely slow downward movement (adjust distance)
            enemy.sety(enemy.ycor() - 0.038)  # Move down by 0.2 units
            # Ensure enemy stays within the screen bounds
            if enemy.xcor() < -280 or enemy.xcor() > 280:
                enemy.goto(-enemy.xcor(), enemy.ycor())  #

    def delete_enemy(self, enemy):
        enemy.hideturtle()
        self.enemies.remove(enemy)

    def no_more_enemies(self):
        return len(self.enemies) == 0
