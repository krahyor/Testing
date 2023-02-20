from hackkerank.alternatingCharacter import *

import unittest

class TestAlternatingCharacter(unittest.TestCase):
    def test_AAAA_in_alternating(self):
        x = 'AAAA'
        result = alternatingCharacter(x)
        self.assertEqual(result,3)
    def test_BBBBB_in_alternating(self):
        x = 'BBBBB'
        result = alternatingCharacter(x)
        self.assertEqual(result,4)
    def test_ABABABAB_in_alternating(self):
        x = 'ABABABAB'
        result = alternatingCharacter(x)
        self.assertEqual(result,0)
    def test_BABABA_in_alternating(self):
        x = 'BABABA'
        result = alternatingCharacter(x)
        self.assertEqual(result,0)
    def test_AAABBB_in_alternating(self):
        x = 'AAABBB'
        result = alternatingCharacter(x)
        self.assertEqual(result,4)
if __name__ == '__main__':
    unittest.main()