from cells import Cell
from graphics import Window
import time
import random


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window = None,
        seed: int = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for row in range(self._num_rows):
            buffer_list = []
            for col in range(self._num_cols):
                buffer_list.append(Cell(self._win))
            self._cells.append(buffer_list)
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                self._draw_cell(row, col)

    def _draw_cell(self, row: int, col: int):
        if self._win is None:
            return
        x1 = self._x1 + (col * self._cell_size_x)
        y1 = self._y1 + (row * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[row][col].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows - 1][self._num_cols -
                                        1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, row: int, col: int):
        self._cells[row][col].visited = True
        moves = [
            (0, -1),  # look left
            (-1, 0),  # look up
            (0, 1),  # look right
            (1, 0)  # look down
        ]
        while True:
            queue = []
            for d_row, d_col in moves:
                ni, nj = row + d_row, col + d_col
                if (
                    0 <= ni < self._num_rows
                    and 0 <= nj < self._num_cols
                    and not self._cells[ni][nj].visited
                ):
                    queue.append((ni, nj, d_row, d_col))
            if not queue:
                self._draw_cell(row, col)
                return
            selection = random.choice(queue)
            ni, nj, d_row, d_col = selection

            if d_col == -1:  # moving left
                self._cells[row][col].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False

            elif d_row == -1:  # moving up
                self._cells[row][col].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False

            elif d_col == 1:  # moving right
                self._cells[row][col].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False

            elif d_row == 1:  # moving down
                self._cells[row][col].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False

            self._break_walls_r(ni, nj)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
