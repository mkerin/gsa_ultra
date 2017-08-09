import unittest
import sys
import math
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from q1_trapeziums import GenVector, Area, solution, Intersection, Line, Dist


class TestQ6(unittest.TestCase):
    """
    """
    def setUp(self):
        pass
    
    def test_GenVector(self):
        p1 = (0, 0)
        p2 = (1, 0)
        p3 = (2, 0)
        self.assertEqual(GenVector(p1, p2), GenVector(p2, p1))
        self.assertEqual(GenVector(p1, p2), GenVector(p1, p3))
        # offset
        p4 = (0, 1)
        p5 = (1, 1)
        self.assertEqual(GenVector(p1, p2), GenVector(p4, p5))
        # reverse diagonal
        p7, p6 = (2, 1), (3, 0)
        self.assertEqual(GenVector(p4, p2), GenVector(p6, p7))

    def test_Area(self):
        pair1 = ((0, 0), (0, 1))
        pair2 = ((1, 0), (1, 2))
        unit_vec = GenVector(pair1[0], pair1[1])
        self.assertEqual(Area(pair1, pair2, unit_vec), 1.5)
        # Same area on both sides of rhombus
        s1_pts1, s1_pts2 = ((0, 0), (1, 1)), ((0, 1), (1, 2))
        unit_vec1 = GenVector(s1_pts1[0], s1_pts1[1])
        s2_pts1, s2_pts2 = ((0, 0), (0, 1)), ((1, 1), (1, 2))
        unit_vec2 = GenVector(s2_pts1[0], s2_pts1[1])
        self.assertAlmostEqual(Area(s1_pts1, s1_pts2, unit_vec1),
                               Area(s2_pts1, s2_pts2, unit_vec2))

    def test_Intersection(self):
        pair1, pair2 = ((0, 0), (1, 1)), ((0, 1), (1, 2))
        unit_vec = GenVector(pair1[0], pair1[1])
        
        orth_vec = -1 * unit_vec[0], unit_vec[1]
        L1 = Line(pair1[0], (pair1[0][0] + orth_vec[0], pair1[0][1] + orth_vec[1]))
        L2 = Line(pair2[0], pair2[1])
        x, y = Intersection(L1, L2)

        self.assertEqual(orth_vec, (-1, 1))
        h = Dist(pair1[0], (x, y))
        self.assertAlmostEqual(h, math.sqrt(2) / 2)

    def test_sol(self):
        D = ((0, 0), (1, 0), (1, 1), (0, 1), (1, 2))
        self.assertEqual(solution(D), "3500")


if __name__ == '__main__':
    unittest.main()
