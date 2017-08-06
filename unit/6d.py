import unittest
import sys
from os import path

sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from 6d_stringy import GenT


class TestQ6(unittest.TestCase):
    """
    """
    def setUp(self):
        pass
    
    def test_n4_k2_v2(self):
        T = [8, 5, 2, 1]
        self.assertEqual(GenT(4, 2, 2), T)

    def test_n4_k2_v0(self):
        T = [1, 2, 5, 8]
        self.assertEqual(GenT(4, 2, 0), T)




if __name__ == '__main__':
    unittest.main()
