import unittest
import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from q9a_breaking_net import solution


class TestQ9a(unittest.TestCase):
    """
    """
    def setUp(self):
        pass

    def test_solution(self):
        self.assertEqual(solution(1), 1)
        self.assertEqual(solution(2), 2)
        self.assertEqual(solution(3), 3)
        self.assertEqual(solution(4), 5)
        self.assertEqual(solution(5), 6)
        self.assertEqual(solution(7), 11)


if __name__ == '__main__':
    unittest.main()
