import unittest
import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from q11_cool_sequences import GenL, GenSwaps


class TestQ11(unittest.TestCase):
    """
    """
    def setUp(self):
        pass
    
    def test_n36(self):
        n = 36
        L = 24
        swaps = 7
        self.assertEqual(GenL(n), L)
        self.assertEqual(GenSwaps(n), swaps)


if __name__ == '__main__':
    unittest.main()
