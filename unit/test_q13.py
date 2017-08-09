import unittest
import sys
import math
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from q13_dragons import GenMidpoints, XYtoTheta, DistFromOrigin, Point, solution, Midpoint


class TestQ13(unittest.TestCase):
    """
    """
    def setUp(self):
        pass
    
    def test_GenMidpoints(self):
        pass
    
    def test_DistFromOrigin(self):
        painting = (1, 0, 0, 1)
        midpoint = Midpoint(1, 1, XYtoTheta(1, 1))
        ans = 1.0 / math.sqrt(2)
        self.assertAlmostEqual(DistFromOrigin(midpoint, painting), ans)

    def test_solution(self):
        T = ((-30, 150, 20, 150),
             (-80, 60, -20, 100),
             (-101, -50, -75, -65),
             (80, 60, 85, 90),
             (85, 100, 90, 10),
             (10, -150, 30, -145),
             (15, -100, 100, -20),
             (82, -90, 95, -40))
        self.assertEqual(solution(T), 7)
        with open("q13_input.txt") as f:
            T = []
            for line in f:
                p = [int(x) for x in line.rstrip("/n").split()]
                T.append(tuple(p))
        T = tuple(T)
        self.assertEqual(solution(T), 289)

    def test_midpoint(self):
        m = Midpoint(1, 0, math.pi)
        m.pids_inline = set([1, 2, 3])
        self.assertEqual(m.pid, None)
        self.assertEqual(m.side, None)
        self.assertEqual(m.pids_inline, set([1, 2, 3]))
        

if __name__ == '__main__':
    unittest.main()
