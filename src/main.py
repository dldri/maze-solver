from graphics import Window
from cells import Cell


def main():
    width = 800
    height = 600
    win = Window(width, height)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(200, 200, 300, 300)
    c2 = Cell(win)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(300, 200, 400, 300)
    c3 = Cell(win)
    c3.has_top_wall = False
    c3.draw(300, 300, 400, 400)

    c1.draw_move(c2, True)
    c2.draw_move(c3)

    win.wait_for_close()


if __name__ == "__main__":
    main()
