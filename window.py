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