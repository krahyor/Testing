from src.hackkerank.alternate import *
import unittest

class TestAlternate(unittest.TestCase):
    def test_alternate_1(self):
        result = alternate('beabeefeab')
        self.assertEqual(result, 5)

    def test_alternate_2(self):
        result = alternate('abaacdabd')
        self.assertEqual(result, 4)

    def test_alternate_3(self):
        result = alternate('asdcbsdcagfsdbgdfanfghbsfdab')
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()