import time
import turtle as t

from food import Food
from snake import Snake
from scoreborad import ScoreBoard


screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
x_index = [0, -20, -40]
screen.tracer(0)
segments = []

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 17:
        scoreboard.scoring()
        food.refresh()
        snake.extend()
        scoreboard.scoring()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        is_game_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
