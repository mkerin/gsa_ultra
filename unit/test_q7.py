import unittest
import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from q7_shouting_array import solution, Permute


class TestQ6(unittest.TestCase):
    """
    """
    def setUp(self):
        pass
    
    def test_Permute(self):
        self.assertEqual(Permute(2, 2), 2)
        self.assertEqual(Permute(2, 3), 0)
        self.assertEqual(Permute(3, 3), 6)

    def test_solution(self):
        self.assertEqual(solution(2), 14)
        self.assertEqual(solution(3), 57)


if __name__ == '__main__':
    unittest.main()
