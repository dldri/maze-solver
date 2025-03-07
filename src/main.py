from graphics import Window
from cells import Cell
from maze import Maze


def main():
    width = 800
    height = 600
    win = Window(width, height)
    maze = Maze(100, 100, 10, 10, 20, 20, win)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
