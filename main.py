import time
from turtle import Turtle,Screen
from scoreboard import ScoreBoard

from snake import Snake
from food import Food

T = 0.1

screen = Screen()
screen.setup(600,600)

screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)


snake = Snake()

food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


scorer = ScoreBoard()










game_is_on = True



while game_is_on:

    ##collision with wall

    if snake.head.xcor() > 280 or  snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_is_on= False
        scorer.game_over()

    ##collision with tail , if head collides with any other segment

    for segment in snake.segments:

        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on= False
            scorer.game_over()

    screen.update()
    time.sleep(T)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        scorer.increase_score()
        snake.extend()
        T-=0.007















































screen.exitonclick()