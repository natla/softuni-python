class Figure:
    def __init__(self, center_x, center_y, color="black", **kwargs):
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

        if any(v is None for v in (self.center_x, self.center_y, self.color)):
            raise ValueError('Value missing')

    def __str__(self):
        return "Figure center: {}:{}, color: {}".format(
            self.center_x,
            self.center_y,
            self.color
        )

    def draw(self, turtle):
        turtle.color(self.color)
        turtle.speed("fastest")

    def jump_to(self, turtle, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
