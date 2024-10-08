import turtle
from rocket import Rocket
from bullets import Bullets
from enemy import Enemy

# Setup screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Shooter")
screen.tracer(0)  # Disable automatic screen updates for manual control

# Prompt for number of enemies from the user
num_enemies = screen.numinput("Enemies", "How many enemies do you want? (Max: 8)", default=5, minval=1, maxval=8)
num_enemies = int(num_enemies)

# Initialize rocket, bullets, and enemies
rocket = Rocket()            # Creates the rocket controlled by the player
rocket_velocity = 0          # Initialize rocket velocity

enemy_group = Enemy(num_enemies)  # Create an enemy group with a specified number of enemies
bullets = Bullets(rocket)         # Create bullets object linked to the rocket for shooting

# Rocket movement functions
def move_rocket():
    # Updates the rocket's x position based on its velocity, keeping it within screen bounds
    global rocket_velocity
    new_x = rocket.xcor() + rocket_velocity
    if -280 < new_x < 280:  # Ensure rocket stays within screen bounds
        rocket.setx(new_x)

def move_left():
    # Moves the rocket left by setting a negative velocity
    global rocket_velocity
    rocket_velocity = -0.4

def move_right():
    # Moves the rocket right by setting a positive velocity
    global rocket_velocity
    rocket_velocity = 0.4

def stop_movement():
    # Stops the rocket's horizontal movement by setting velocity to 0
    global rocket_velocity
    rocket_velocity = 0

# Keyboard bindings for controlling the rocket and shooting
screen.listen()
screen.onkeypress(move_left, "Left")    # Move left on Left arrow key press
screen.onkeyrelease(stop_movement, "Left")  # Stop moving when Left arrow key is released
screen.onkeypress(move_right, "Right")  # Move right on Right arrow key press
screen.onkeyrelease(stop_movement, "Right") # Stop moving when Right arrow key is released
screen.onkeypress(bullets.shoot, "space")   # Shoot bullets on Spacebar press

# Main game loop
game_over = False
while not game_over:
    move_rocket()           # Update the rocket's position
    bullets.update()        # Update the bullets' positions
    enemy_group.move()      # Update the enemies' positions

    # Check for collisions between bullets and enemies
    for bullet in bullets.bullets[:]:
        for enemy in enemy_group.enemies[:]:
            if bullet.distance(enemy) < 20:  # Collision check within 20 units
                enemy_group.delete_enemy(enemy)  # Remove the enemy if hit
                bullets.delete_bullet(bullet)    # Remove the bullet that hit the enemy

    # Check if any enemy reaches the bottom of the screen
    for enemy in enemy_group.enemies:
        if enemy.ycor() < -190:   # Game over if enemy reaches y-coordinate -190
            print("Game Over - Enemies crossed your territory!")
            game_over = True
            break

    # Check if all enemies have been destroyed
    if enemy_group.no_more_enemies():
        print("Congratulations! You win!")
        game_over = True

    screen.update()   # Update the screen manually since tracer(0) disables automatic updates

# Close the screen when the game is over
screen.bye()
