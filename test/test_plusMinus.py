from src.plusMinus import *
import unittest

class TestPlusMinus(unittest.TestCase):

    def test_plusMinus(self):
        self.assertEqual(plusMinus([-4, 3, -9, 0, 4, 1]), (3, 2, 1))
        self.assertEqual(plusMinus([1, 2, 3, -1, -2, -3, 0, 0]), (3, 3, 2))
        self.assertEqual(plusMinus([0, 0, 0, 0, 0]), (0, 0, 5))
        self.assertEqual(plusMinus([1, -1, 1, -1, 1, -1]), (3, 3, 0))
        self.assertEqual(plusMinus([0, -1, -1, 1, 1]), (2, 2, 1))
        self.assertEqual(plusMinus([2, 2, 2, 2, 2, 2]), (6, 0, 0))

if __name__ == '__main__':
    unittest.main()