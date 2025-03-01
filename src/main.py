from classes import (
    Window,
    Point,
    Line
)
import random


def main():
    width = 800
    height = 600
    win = Window(width, height)
    p1 = Point(random.randint(0, width),
               random.randint(0, height))
    p2 = Point(random.randint(0, width),
               random.randint(0, height))
    p3 = Point(random.randint(0, width),
               random.randint(0, height))
    p4 = Point(random.randint(0, width),
               random.randint(0, height))
    p5 = Point(random.randint(0, width),
               random.randint(0, height))
    p6 = Point(random.randint(0, width),
               random.randint(0, height))
    points = [p1, p2, p3, p4, p5, p6]
    colours = ["black", "red", "blue", "green", "cyan"]
    for i in range(10):
        point1 = random.choice(points)
        point2 = random.choice(points)
        line = Line(point1, point2)
        fill_colour = random.choice(colours)
        win.draw_line(line, fill_colour)
        print(
            f"Drawing a {fill_colour} line between points {point1} and {point2}")

    win.wait_for_close()


if __name__ == "__main__":
    main()
