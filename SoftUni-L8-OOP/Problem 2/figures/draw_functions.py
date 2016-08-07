import os
import json
import turtle

from figures.simple_figures import Circle, Square, Rectangle, Pie, RegularPolygon
from loaders.loader import JSONLoader, YAMLLoader


def main():
    try:
        input_data = load_input_data("figures_simple.json")
        figures = create_figures(input_data)
        draw_figures(figures)
    except Exception as e:
        print("Invalid input file provided! Error:", e)


def load_input_data(input_filename):
    filename, extension = os.path.splitext(input_filename)
    loader = None
    if extension == '.json':
        loader = JSONLoader(input_filename)
    elif extension == '.yaml':
        loader = YAMLLoader(input_filename)

    if loader is not None:
        return loader.load()
    else:
        raise ValueError("Unsupported file format: {}".format(extension))


FIGURE_TYPES = {
    'square': Square,
    'circle': Circle,
    'rectangle': Rectangle,
    'pie': Pie,
    'reg_polygon': RegularPolygon
}


def create_figures(input_data: dict) -> list: 
    result = []
    for f_info in input_data:
        figure_type = f_info['type']
        if figure_type in FIGURE_TYPES:
            figure_class = FIGURE_TYPES[figure_type]
            result.append(figure_class(**f_info))
        else:
            raise ValueError('Unsupported figure')
    return result


def draw_figures(figures):
    for figure in figures:
        t = turtle.Turtle()
        t.speed('fast')
        figure.draw(t)

    turtle.exitonclick()


if __name__ == "__main__":  
    main()
