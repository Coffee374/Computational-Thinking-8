#makes the turtle come
import turtle

#does the background
turtle.Screen().bgcolor("black")

#sets up the pink turtle
t = turtle.Turtle()
t.speed(100)
t.color("pink")

for i in range(30) :
    t.forward(100)
    t.right(90)
    t.forward(1)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(1)
    t.left(90)

    turtle.exitonclick()