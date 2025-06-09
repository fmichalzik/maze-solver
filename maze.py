from window import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        if self.num_rows < 0 or self.num_cols < 0:
            raise Exception("The number of rows and coloumns has to be postitiv!")
        for i in range(self.num_cols):
            self.__cells.append([])
            for j in range(self.num_rows):
                cell_j = Cell(self.win)
                self.__cells[i].append(cell_j)
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        x2 = x1 + self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        y2 = y1 + self.cell_size_y
        self.__cells[i][j].draw(x1, x2, y1, y2)
        self.__animate()

    def __animate(self):
        if self.win:
            self.win.redraw()
            time.sleep(0.0015)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)
