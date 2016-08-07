import json
import turtle

from figures.simple_figures import Circle, Square, Rectangle, Pie, RegularPolygon


def main():
    try:
        input_data = load_input_data("figures_simple.json")
        figures = create_figures(input_data)
        draw_figures(figures)
    except Exception as e:
        print("Invalid input file provided! Error:", e)


def load_input_data(input_filename):
    with open(input_filename) as f:
        input_data = json.load(f)
        return input_data

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
