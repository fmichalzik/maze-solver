from window import Window, Point, Line

def main():
    win = Window(800, 600)

    test_line = Line(Point(50, 50), Point(400, 400))

    win.draw_line(test_line)
    win.wait_for_close()
main()