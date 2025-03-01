from graphics import (
    Window,
    Point,
    Line
)


class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = win

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.has_left_wall == True:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)

        if self.has_top_wall == True:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)

        if self.has_right_wall == True:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line)

        if self.has_bottom_wall == True:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)
