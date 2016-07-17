# Using cycles, arithmetics, if statements and/or logical operators,
# make the turtle draw "interesting stuff". 

import turtle
turtle.speed('fastest')

turtle.penup()
turtle.goto(-300, -50)
turtle.pendown()

for i in range(10, 2300):
    turtle.right(i ** 2)
    turtle.backward(5)

turtle.exitonclick()
