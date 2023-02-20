from src.area import *
import unittest

class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1), 1)
        self.assertEqual(area(2), 4)
        self.assertEqual(area(-3), 9)

    def test_areaTriangle(self):
        self.assertEqual(areaTriangle(0, 0), 0)
        self.assertEqual(areaTriangle(2, 3), 3)
        self.assertEqual(areaTriangle(4, 1), 2)
        self.assertEqual(areaTriangle(-3, 5), -7.5)

if __name__ == '__main__':
    unittest.main()