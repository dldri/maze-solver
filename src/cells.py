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

    def get_centre(self):
        self_centre_x = (self.__x1 + self.__x2) // 2
        self_centre_y = (self.__y1 + self.__y2) // 2
        self_centre = Point(self_centre_x, self_centre_y)

        return self_centre

    def draw_move(self, to_cell: "Cell", undo: bool = False):
        self_centre = self.get_centre()
        to_centre = to_cell.get_centre()
        line = Line(self_centre, to_centre)
        fill_colour = "red"
        if undo:
            fill_colour = "grey"

        self.__win.draw_line(line, fill_colour)
