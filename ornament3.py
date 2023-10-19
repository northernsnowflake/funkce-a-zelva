from turtle import forward, left, right, exitonclick, penup, pendown, speed, circle
speed=0


penup()
left(90)
pendown()
for b in range(360):
    forward(1+b/20)
    left(15)


exitonclick()
