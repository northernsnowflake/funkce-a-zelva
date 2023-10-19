from turtle import forward, left, right, exitonclick, penup, pendown
n = 5

for b in range (1):
    for a in range(5):
        forward(200/5)
        #left(60)
        left(180*2/5) #vnitrni uhel je 180 * (1-2/n)
    penup()
    forward(100)
    pendown()

    for a in range(6):
        forward(200/6)
        #left(60)
        left(180*2/6)
    penup()
    forward(100)
    pendown()

    for a in range(7):
        forward(200/7)
        #left(60)
        left(180*2/7)
    penup()
    forward(100)
    pendown()

    for a in range(8):
        forward(200/8)
        #left(60)
        left(180*2/8)
    penup()
    forward(100)
    pendown()

exitonclick()
