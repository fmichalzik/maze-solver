from window import Window, Point, Line, Cell

def main():
    win = Window(800, 600)

    """ test_line = Line(Point(50, 50), Point(400, 400))

    win.draw_line(test_line) """

    test_cell_a = Cell(win)
    test_cell_b = Cell(win)
    test_cell_c = Cell(win)
    test_cell_a.draw(100, 150, 100, 150)
    test_cell_b.draw(200, 250, 200, 250)
    test_cell_c.draw(400, 450, 100, 150)

    test_cell_a.draw_move(test_cell_c)
    test_cell_c.draw_move(test_cell_b)

    win.wait_for_close()
main()