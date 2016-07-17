import turtle

turtle.speed('slow')

side = int(input('Input the length of the figure side: '))
angle = int(input('Input the angle of the figure: '))

while True:
    turtle.forward(side)
    turtle.right(angle)


turtle.exitonclick()
