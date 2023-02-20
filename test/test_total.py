from src.total import *
import unittest

class TestTotal(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total(2,3),5)
        self.assertEqual(total(0, 0), 0)
        self.assertEqual(total(-2, 2), 0)
        self.assertEqual(total(1000000, 1), 1000001)

if __name__ == '__main__':
    unittest.main()
