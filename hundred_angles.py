#Nakresli pravidelný stoúhelník.



from turtle import forward, left, right, exitonclick, penup, pendown

side = 100
for a in range(side):
    forward(200/side)
    left(180*2/side)


exitonclick()
