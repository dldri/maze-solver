from graphics import Window
from cells import Cell


def main():
    width = 800
    height = 600
    win = Window(width, height)

    Cell(win).draw(200, 200, 300, 300)
    Cell(win).draw(300, 300, 400, 400)

    win.wait_for_close()


if __name__ == "__main__":
    main()
