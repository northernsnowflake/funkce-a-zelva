from turtle import forward, left, right, exitonclick, penup, pendown, shape
from math import sqrt

for b in range (1):
    #for a in range(1):

        left(180)
        forward(100)
        #forward(sqrt(2)*100)
        right(135)
        forward(sqrt(2)*100)

        left(90)
        forward(sqrt(2)*100/2)

        left(90)
        forward(sqrt(2)*100/2)

        left(135)
        forward(100)

        right(90)
        forward(100)

        right(135)
        forward(sqrt(2)*100)

        left(135)
        forward(100)


exitonclick()
