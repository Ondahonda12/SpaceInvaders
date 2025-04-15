# Imports
import turtle
import math
import random
try:
    # Screen setup
    screen = turtle.Screen()
    screen.title("Space Invaders")
    screen.bgcolor("white")
    enemy_count = int(screen.numinput("Enter number of enemies", "1-10", 8, minval=1, maxval=10))

    # Game border
    border = turtle.Turtle()
    border.speed(0)
    border.color("black")
    border.penup()
    border.setposition(-300, -300)
    border.pendown()
    border.pensize(10)
    for side in range(4):
        border.forward(600)
        border.left(90)
    border.hideturtle()

    # Player
    player = turtle.Turtle()
    player.color("black")
    player.shape("triangle")
    player.speed(0)
    player.penup()
    player.setposition(0, -285)
    player.setheading(90)

    # Bullet
    bullet = turtle.Turtle()
    bullet.color("black")
    bullet.shape("circle")
    bullet.penup()
    bullet.speed(0)
    bullet.shapesize(0.25, 0.25)
    bullet.hideturtle()
    bullet_speed = 40
    bullet_state = "ready"

    # Movement functions
    def move_left():
        x = player.xcor()
        x -= 10
        if x < -280:
            x = -280
        player.setx(x)

    def move_right():
        x = player.xcor()
        x += 10
        if x > 280:
            x = 280
        player.setx(x)

    def fire_bullet():
        global bullet_state
        if bullet_state == "ready":
            bullet_state = "fire"
            x = player.xcor()
            y = player.ycor() + 10
            bullet.setposition(x, y)
            bullet.showturtle()

    # Keyboard bindings
    turtle.onkey(fire_bullet, "space")
    turtle.onkeypress(move_left, "Left")
    turtle.onkeypress(move_right, "Right")
    turtle.listen()

    # Enemies
    enemies = []
    start_x = -250
    start_y = 250
    for i in range(enemy_count):
        enemies.append(turtle.Turtle())
    for enemy in enemies:
        start_x += 50
        enemy.shape("circle")
        enemy.color("black")
        enemy.penup()
        enemy.speed(0)
        enemy.setposition(start_x, start_y)

    enemy_speed = 5

    # Collision check
    def is_collision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
        return distance < 18

    # Game loop
    score = 0

    while True:
        screen.delay(1)
        index = -1

        # Bullet movement
        if bullet_state == "fire":
            y = bullet.ycor()
            y += bullet_speed
            bullet.sety(y)

        if bullet.ycor() > 275:
            bullet.hideturtle()
            bullet_state = "ready"

        for enemy in enemies:
            index += 1
            x = enemy.xcor()
            x += enemy_speed
            enemy.setx(x)

            # Move enemy down and reverse
            if enemy.xcor() > 280 or enemy.xcor() < -280:
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                enemy_speed *= -1

            if is_collision(bullet, enemy):
                bullet.hideturtle()
                bullet.setposition(0, -400)
                bullet_state = "ready"
                score += 1
                enemy.hideturtle()
                del enemies[index]
                if score == enemy_count:
                    player.hideturtle()
                    gameover = turtle.Turtle()
                    gameover.speed(1)
                    gameover.color('green')
                    style = ('Times New Roman', 50, 'bold')
                    gameover.write('YOU WIN!', font=style, align='center')
                    gameover.hideturtle()
                    break

            if is_collision(player, enemy) or enemy.ycor() < -285:
                player.hideturtle()
                for e in enemies:
                    e.hideturtle()
                gameover = turtle.Turtle()
                gameover.speed(0)
                gameover.color('red')
                style = ('Times New Roman', 50, 'bold')
                gameover.write('GAME OVER!', font=style, align='center')
                gameover.hideturtle()
                break
except:
    print("An error occurred. Please check the code and try again.")

     
       
    
 


   
        
    



