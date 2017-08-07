import unittest
import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from q6_stringy import GenT, GenDist


class TestQ6(unittest.TestCase):
    """
    """
    def setUp(self):
        pass
    
    def test_n2_k2_v2(self):
        n, k, v = 2, 2, 2
        T = [[1, 1, 1, 0], [0, 0, 0, 1]]
        self.assertEqual(GenT(n, k, v), T)

    def test_n3_k2_v2(self):
        n, k, v = 3, 2, 2
        T = [[2, 2, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]
        dist = [5, 2, 1]
        self.assertEqual(GenT(n, k, v), T)
        self.assertEqual(GenDist(GenT(n, k, v)), dist)

    def test_n4_k2_v2(self):
        n, k, v = 4, 2, 2
        T = [[3, 3, 2, 0], [1, 1, 1, 2], [0, 0, 1, 1],
             [0, 0, 0, 1]]
        dist = [8, 5, 2, 1]
        self.assertEqual(GenT(n, k, v), T)
        self.assertEqual(GenDist(GenT(n, k, v)), dist)



if __name__ == '__main__':
    unittest.main()
