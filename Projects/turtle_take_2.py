#makes the turtle come
import turtle

#does the background
turtle.Screen().bgcolor("black")

#sets up the pink turtle
t = turtle.Turtle()
t.speed(100)
t.color("pink")
t.penup()
t.goto(-350,200)
t.pendown()

#sets up the blue turtle
t2 = turtle.Turtle()
t2.speed(100)
t2.color("skyblue")
t2.penup()
t2.goto(-350,300)
t2.pendown()

#sets up the white turtle
t3 = turtle.Turtle()
t3.speed(100)
t3.color("white")
t3.penup()
t3.goto(-350,100)
t3.pendown()

#sets up the 2nd pink turtle
t4 = turtle.Turtle()
t4.speed(100)
t4.color("pink")
t4.penup()
t4.goto(-350,0)
t4.pendown()

#sets up the 2nd blue turtle
t5 = turtle.Turtle()
t5.speed(100)
t5.color("skyblue")
t5.penup()
t5.goto(-350,-100)
t5.pendown()


for i in range(50) :
    t2.forward(700)
    t2.right(90)
    t2.forward(1)
    t2.right(90)
    t2.forward(700)
    t2.left(90)
    t2.forward(1)
    t2.left(90)

for i in range(50) :
    t.forward(700)
    t.right(90)
    t.forward(1)
    t.right(90)
    t.forward(700)
    t.left(90)
    t.forward(1)
    t.left(90)

for i in range(50) :
    t3.forward(700)
    t3.right(90)
    t3.forward(1)
    t3.right(90)
    t3.forward(700)
    t3.left(90)
    t3.forward(1)
    t3.left(90)

for i in range(50) :
    t4.forward(700)
    t4.right(90)
    t4.forward(1)
    t4.right(90)
    t4.forward(700)
    t4.left(90)
    t4.forward(1)
    t4.left(90)

for i in range(50) :
    t5.forward(700)
    t5.right(90)
    t5.forward(1)
    t5.right(90)
    t5.forward(700)
    t5.left(90)
    t5.forward(1)
    t5.left(90)

turtle.exitonclick()