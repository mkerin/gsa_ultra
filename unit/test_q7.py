import unittest
import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from q7_shouting_array import solution, nPk, nCk


class TestQ6(unittest.TestCase):
    """
    """
    def setUp(self):
        pass
    
    def test_nPk(self):
        self.assertEqual(nPk(2, 2), 2)
        self.assertEqual(nPk(2, 3), 0)
        self.assertEqual(nPk(3, 3), 6)

    def test_solution(self):
        self.assertEqual(solution(2), 14)
        self.assertEqual(solution(3), 57)

    def test_nCk(self):
        self.assertEqual(nCk(6, 2), 15)


if __name__ == '__main__':
    unittest.main()
