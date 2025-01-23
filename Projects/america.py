#makes the turtle come
import turtle

#does the background
turtle.Screen().bgcolor("black")

#sets up the stripes turtle
t = turtle.Turtle()
t.speed(100)
t.color("red")
t.penup()
t.goto(-350,300)
t.pendown()

#sets up the blue square turtle
t2 = turtle.Turtle()
t2.speed(100)
t2.color("blue")
t2.penup()
t2.goto(-350,300)
t2.pendown()

#sets up the star turtle (probably really shity)
t3 = turtle.Turtle()
t3.speed(100)
t3.color("white")
t3.penup()
t3.goto(-300,200)
t3.pendown()


for i in range(6) :
    for i in range(20) :
        t.forward(700)
        t.right(90)
        t.forward(1)
        t.right(90)
        t.forward(700)
        t.left(90)
        t.forward(1)
        t.left(90)

    t.color("red")

    for i in range(20) :
        t.forward(700)
        t.right(90)
        t.forward(1)
        t.right(90)
        t.forward(700)
        t.left(90)
        t.forward(1)
        t.left(90)

    t.color("white")

for i in range(110) :
    t2.forward(300)
    t2.right(90)
    t2.forward(1)
    t2.right(90)
    t2.forward(300)
    t2.left(90)
    t2.forward(1)
    t2.left(90)

for i in range(5):
    t3.forward(50)
    t3.left(45)

turtle.exitonclick()