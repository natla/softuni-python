import turtle

turtle.speed('slow')

side = int(input('Input the length of the square side: '))

count = 0
while count < 4:
    turtle.forward(side)
    turtle.right(90)
    count += 1

turtle.exitonclick()
