from src.CatAndMouse import *
import unittest

class TestCatAndMouse(unittest.TestCase):

    def test_cat_and_mouse(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")
        self.assertEqual(cat_and_mouse(1, 4, 2), "Cat A")
        self.assertEqual(cat_and_mouse(1, 2, 3), "Cat B")
        self.assertEqual(cat_and_mouse(2, 1, 3), "Cat A")
        self.assertEqual(cat_and_mouse(3, 2, 1), "Cat B")
        self.assertEqual(cat_and_mouse(3, 1, 2), "Mouse C")

if __name__ == '__main__':
    unittest.main()



