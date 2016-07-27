import turtle
g = 134
l = 120
count = 0
max_count = int(input("Enter the number of lines the turtle should draw: "))

while count < max_count:
    turtle.left(g)
    turtle.forward(l)
    count += 1

turtle.exitonclick()
