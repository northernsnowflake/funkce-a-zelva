from turtle import forward, left, right, exitonclick, penup, pendown
#speed=3
x=5

penup()
right(45)
#forward(5)
pendown()
for b in range(15):
    for a in range (4):
        left(45)
        forward(x)
    x = x+5

exitonclick()
