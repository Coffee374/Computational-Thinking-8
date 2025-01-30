#sets stuff up
import turtle
import random
import time

#sets speed and stuff
rotation_speed = 0.5
spawn_interval = 0.05
ball_speed = 2

#sets up window
window = turtle.Screen()
window.tracer(0)
spinner = turtle.Turtle()

#spawn new balls
color = random.random(), random.random(), random.random()
balls = []

def spawn_ball(referance):
    balls.append(turtle.Turtle())
    balls[-1].shape("circle")
    balls[-1].color(color)
    balls[-1].turtlesize()
    balls[-1].penup()
    balls[-1].setposition(referance.position())
    balls[-1].setheading(referance.heading())

#...

#main animation loop
spawn_timer = time.time()
while True:
    spinner.left(rotation_speed)

    #spawn new ball
    if time.time() - spawn_timer > spawn_interval:
        spawn_ball(spinner)
        spawn_timer = time.time()

    #move all balls and clear balls that leave the screen
    for ball in balls.copy():
        ball.forward(ball_speed)
        #check if ball has left the screen
        if (
            abs(ball.xcor()) > window.window_width() / 2
            or abs (ball.ycor()) > window.window_width() / 2
        ):
            ball.hideturtle()
            balls.remove(ball)

    window.update()

turtle.done

#i left off at recycling turtle objects cause i was tired
