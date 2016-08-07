from figures.base import Figure


class Circle(Figure):
    def __init__(self, radius, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius

    def draw(self, turtle):
        super().draw(turtle)
        self.jump_to(turtle, self.center_x,
                     self.center_y - self.radius) 
        turtle.circle(self.radius)
        self.jump_to(turtle, 0, 0)


class Square(Figure):
    def __init__(self, side, **kwargs):
        super().__init__(**kwargs)
        self.side = side

    def draw(self, turtle):
        super().draw(turtle)
        half_side = self.side / 2
        left = self.center_x - half_side
        down = self.center_y - half_side

        self.jump_to(turtle, left, down)
        for _ in range(4):
            turtle.forward(self.side)
            turtle.left(90)
        self.jump_to(turtle, 0, 0)


class Rectangle(Figure):
    def __init__(self, height, width, **kwargs):
        super().__init__(**kwargs)
        self.height = height
        self.width = width

    def draw(self, turtle):
        super().draw(turtle)
        half_width = self.width / 2
        half_height = self.height / 2
        left = self.center_x - half_width
        down = self.center_y - half_height

        self.jump_to(turtle, left, down)
        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)
        self.jump_to(turtle, 0, 0)


class Pie(Figure):
    def __init__(self, radius, arg_degrees, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.arg_degrees = arg_degrees

    def draw(self, turtle):
        super().draw(turtle)
        self.jump_to(turtle, self.center_x,
                     self.center_y - self.radius)
        turtle.begin_fill()
        turtle.circle(self.radius, extent=self.arg_degrees)
        turtle.end_fill()
        self.jump_to(turtle, 0, 0)


class RegularPolygon(Figure):
    def __init__(self, radius, num_sides, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.num_sides = num_sides

    def draw(self, turtle):
        super().draw(turtle)
        angle = 360 / self.num_sides

        self.jump_to(turtle, self.center_x,
                     self.center_y - self.radius)
        turtle.circle(self.radius, steps=self.num_sides)
        self.jump_to(turtle, 0, 0)
