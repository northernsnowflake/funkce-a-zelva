from turtle import forward, left, exitonclick, right
from turtle import speed
speed(0)
for i in range(18):
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)

    left(20)

right(90)
forward(100)
left(65)

m=15
for l in range(2):
    for k in range(100):
        forward(0.5)
        left(1)
    left(80)
    for k in range(100):
        forward(0.5)
        left(1)
    left(m)
    forward(50)
    right(65)
    right(90) # otočení posledního listu
    m=m-140

exitonclick()
