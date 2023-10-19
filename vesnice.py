#vesnice
#Domecek
from turtle import shape, forward, penup, pendown, left, right, exitonclick
from math import sqrt
from turtle import speed
shape('turtle')
speed(10) # hodně rychlá želva

penup()
left(180)
forward(600)
left(180)
pendown()

for _ in range (10):
    forward(100)
    left(135)
    forward(100*sqrt(2))
    right(135)
    forward(100)
    right(135)
    forward(100*sqrt(2))
    right(135)
    forward(100)
    right(45)
    forward(71)
    right(90)
    forward(71)
    right(45)
    forward(100)
    right(90)
    forward(100)

    right (180)
    penup()
    forward(100)
    pendown()
    forward(50)

exitonclick()
