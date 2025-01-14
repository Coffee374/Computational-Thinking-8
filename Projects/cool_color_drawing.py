#makes the turtle come
import turtle

#does the background
turtle.Screen().bgcolor("black")

#sets up the pink turtle
t = turtle.Turtle()
t.speed(100)
t.color("pink")
t.left(20)

#sets up the blue turtle
t2 = turtle.Turtle()
t2.speed(95)
t2.color("skyblue")
t2.left(10)

#sets up the white turtle
t3 = turtle.Turtle()
t3.speed(90)
t3.color("white")
t3.left(0)

#makes the turtles do growing triangles
for i in range(100000) :
    t.forward(1 + i)
    t.left(120 + 1)
    t2.forward(1 + i)
    t2.left(120 + 1)
    t3.forward(1 + i)
    t3.left(120 + 1)

#kills the turtle?
turtle.exitonclick()