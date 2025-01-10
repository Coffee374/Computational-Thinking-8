import turtle

t = turtle.Turtle()
t.speed(100)
t.color("#F98B88")

t2 = turtle.Turtle
t2.speed(99)
t2.color("#87CEEB")
t2.left(10)

for i in range(100000) :
    t.forward(30 + i)
    t.left(120 + 1)
    t2.forward(30 + i)
    t2.left(120 + 1)

turtle.exitonclick()