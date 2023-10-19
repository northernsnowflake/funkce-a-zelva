from turtle import forward, left, right, exitonclick, penup, pendown
side = int(input('Insert number of sides:'))
#side = 100
for a in range(side):
    forward(200/side)
    #left(60)
    left(180*2/side)
'''
for b in range (4):
    for a in range(side):
        forward(200/side)
        #left(60)
        left(180*2/side)
    penup()
    forward(100)
    pendown()
    side = side + 1
'''

exitonclick()
