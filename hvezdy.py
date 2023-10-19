from turtle import forward, left, right, exitonclick, penup, pendown, speed
from random import randrange

pocet = randrange(0,10)

#více hvězd
for b in range(100):
    uhel = randrange(0,360,10)
    velikost = randrange(5,45)
    #1hvězda
    for a in range(5):
        left(45)
        forward(velikost)
        right(117)
        forward(velikost)
    #left(45)

    penup()
    left(uhel)
    forward(100)
    pendown()


exitonclick()
