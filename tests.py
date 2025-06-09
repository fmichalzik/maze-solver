import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells__0(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells), # type: ignore
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]), # type: ignore
            num_rows,
        )

    def test_maze_create_cells__1(self):
        num_cols = 11
        num_rows = 111
        m1 = Maze(11, 111, num_rows, num_cols, 11, 11)
        self.assertEqual(
            len(m1._Maze__cells), # type: ignore
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]), # type: ignore
            num_rows,
        )
    
    def test_maze_create_cells__2(self):
        num_cols = 20
        num_rows = 20
        m1 = Maze(20, 20, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells), # type: ignore
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]), # type: ignore
            num_rows,
        )
    
    def test_maze_create_cells__negativ_0(self):
        num_cols = 20
        num_rows = 20
        m1 = Maze(-20, -20, num_rows, num_cols, -10, -10)
        self.assertEqual(
            len(m1._Maze__cells), # type: ignore
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]), # type: ignore
            num_rows,
        )

    def test_maze_create_cells__negativ_1(self):
        with self.assertRaises(Exception):
            num_cols = -20
            num_rows = -20
            m1 = Maze(-20, -20, num_rows, num_cols, -10, -10)

    def test_maze_create_cells__entrance(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_entrance_and_exit() # type: ignore
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall, # type: ignore
            False,
        )
        self.assertEqual(
            m1._Maze__cells[-1][-1].has_bottom_wall, # type: ignore
            False,
        )

    def test_maze_create_cells__visited_true(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_walls_r(0,0) # type: ignore
        self.assertEqual(
            m1._Maze__cells[0][0].visited, # type: ignore
            True,
        )
        self.assertEqual(
            m1._Maze__cells[-int(num_cols/2)][-int(num_rows/2)].visited, # type: ignore
            True,
        )
        self.assertEqual(
            m1._Maze__cells[-1][-1].visited, # type: ignore
            True,
        )

    def test_maze_create_cells__visited_reset(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_walls_r(0,0) # type: ignore
        m1._Maze__reset_cells_visited() # type: ignore
        self.assertEqual(
            m1._Maze__cells[0][0].visited, # type: ignore
            False,
        )
        self.assertEqual(
            m1._Maze__cells[-int(num_cols/2)][-int(num_rows/2)].visited, # type: ignore
            False,
        )
        self.assertEqual(
            m1._Maze__cells[-1][-1].visited, # type: ignore
            False,
        )

if __name__ == "__main__":
        unittest.main()
