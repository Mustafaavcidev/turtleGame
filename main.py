import turtle
import random
import time

# screen
screen = turtle.Screen()
screen.bgcolor("ivory1")
screen.title("catch the turtle")

y = screen.window_height() / 2
top_height = y * 0.9

FONT = ("Arial", 20, "normal")

score = 0
game_time = 20

# turtle
turtle_instance = turtle.Turtle()
turtle_instance.speed(0)
turtle_instance.shape("turtle")
turtle_instance.shapesize(1, 1)

# text
turtle_text = turtle.Turtle()
turtle_text.color("dark green")
turtle_text.speed(0)
turtle_text.hideturtle()
turtle_text.penup()
turtle_text.goto(0, top_height)
turtle_text.write("Score: ", move=False, align="center", font=FONT)


turtle_time = turtle.Turtle()
turtle_time.color("red")
turtle_time.speed(0)
turtle_time.hideturtle()
turtle_time.penup()
turtle_time.goto(0, top_height - 40)
turtle_time.write("Time: ", move=False, align="center", font=FONT)

max_x = screen.window_height() // 3
max_y = screen.window_width() // 3
def randomly_turtle(turtle_obj):
    turtle_obj.penup()
    new_x = random.randint(-max_x, max_x)
    new_y = random.randint(-max_y, max_y)
    turtle_obj.goto(new_x,new_y)
def check_click(x,y):
    global score
    if -max_x < x < max_x and -max_y < y < max_y:
        score += 1
        turtle_text.clear()
        turtle_text.write(f"Score: {score}", move=False, align="center", font=FONT )


def restart_turtle():
    global score, game_time

    score = 0
    game_time = 20

    turtle_text.clear()
    turtle_text.write(f"Score: {score}", move=False, align="center", font=FONT)

    turtle_time.clear()
    turtle_time.write(f"Time: {game_time}", move=False, align="center", font=FONT)

    turtle_instance.setposition(0,0)
    time.sleep(1)

def quit_game():
    turtle_text.clear()
    turtle_quit = turtle.Turtle()
    turtle_quit.hideturtle()
    turtle_instance.hideturtle()
    turtle_quit.speed(0)
    turtle_quit.color("dark blue")
    turtle_quit.write("being closed, please wait !!", move=False, align="center", font=FONT)
    time.sleep(2)
    turtle.bye()
def main_game():
    global game_time
    while game_time > 0:
        randomly_turtle(turtle_instance)
        time.sleep(1)
        game_time -= 1
        turtle_time.clear()
        turtle_time.write(f"Time: {game_time}", move=False, align="center", font=FONT)

    turtle_time.clear()
    turtle_time.write("Time's up!", move=False, align="center", font=FONT)

    turtle_text.clear()
    turtle_text.write(f"New Score: {score}", move=False, align="center", font=FONT)
    turtle_instance.hideturtle()
    time.sleep(3)


turtle_instance.onclick(lambda x,y : check_click(x,y))
turtle.listen()
turtle.onkey(quit_game, "q")
turtle.onkey(restart_turtle, "r")
main_game()
turtle.bye()
