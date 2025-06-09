from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze-Solver")
        self.canvas = Canvas(self.root, bg = "white", width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.window_running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point_a.x, self.point_a.y,
            self.point_b.x, self.point_b.y,
            fill = fill_color, width = 2
        )

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True 
        self.has_top_wall = True   
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
    
    def draw(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            if self.__win:
                self.__win.draw_line(left_wall)
        else:
            left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            if self.__win:
                self.__win.draw_line(left_wall, "white")

        if self.has_right_wall:
            right_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            if self.__win:
                self.__win.draw_line(right_wall)
        else:
            right_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            if self.__win:
                self.__win.draw_line(right_wall, "white")
        
        if self.has_top_wall:
            top_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            if self.__win:
                self.__win.draw_line(top_wall)
        else:
            top_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            if self.__win:
                self.__win.draw_line(top_wall, "white")

        if self.has_bottom_wall:
            bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            if self.__win:
                self.__win.draw_line(bottom_wall)
        else:
            bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            if self.__win:
                self.__win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        line = Line(Point(self.__x1 + ((self.__x2 - self.__x1) / 2), self.__y1 + ((self.__y2 - self.__y1) / 2)),
                     Point(to_cell.__x1 + ((to_cell.__x2 - to_cell.__x1) / 2), to_cell.__y1 + ((to_cell.__y2 - to_cell.__y1) / 2)))
        if not undo:
            if self.__win:
                self.__win.draw_line(line, "red")
                return
        if self.__win:
            self.__win.draw_line(line, "gray")