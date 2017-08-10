import unittest
import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from q12_triangles import solution


class TestQ6(unittest.TestCase):
    """
    """
    def setUp(self):
        pass

    def test_solution(self):
        self.assertEqual(solution(0), 0)
        self.assertEqual(solution(1), 6)
        self.assertEqual(solution(2), 24)
        self.assertEqual(solution(3), 60)


if __name__ == '__main__':
    unittest.main()
