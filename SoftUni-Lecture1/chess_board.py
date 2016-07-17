import turtle

turtle.speed('fastest')

side = 40
n = 1
for j in range(8):
    for i in range(8):
        if i % 2 == 0 and j % 2 == 0 \
                or i % 2 != 0 and j % 2 != 0:
            turtle.begin_fill()
        for m in range(4):
            turtle.forward(side)
            turtle.right(90)
        turtle.end_fill()
        turtle.forward(side)

    turtle.penup()
    turtle.goto(0, n * side)
    turtle.pendown()
    n += 1

turtle.exitonclick()
