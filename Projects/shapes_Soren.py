import turtle

t = turtle.Turtle()
t.penup()
t.speed(20)
t.goto(-300,200)
t.color("red")
t.pendown()

for i in range(10):
    for i in range(4):
        t.forward(40)
        t.left(90)
    t.penup()
    t.forward(60)
    t.pendown()

turtle.exitonclick()
    