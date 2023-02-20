from src.volum import *
import unittest
import math

class TestShapes(unittest.TestCase):

    def test_cubic(self):
        self.assertEqual(cubic(2), 8)
        self.assertEqual(cubic(0), 0)
        self.assertEqual(cubic(-3), -27)

    def test_cylinder(self):
        self.assertAlmostEqual(cylinder(1, 1), math.pi, places=5)
        self.assertAlmostEqual(cylinder(2, 3), 37.6991118, places=5)
        self.assertAlmostEqual(cylinder(0, 4), 0, places=5)
        self.assertAlmostEqual(cylinder(-1, 1), math.pi, places=5)

if __name__ == '__main__':
    unittest.main()


