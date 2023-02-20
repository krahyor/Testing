from src.hackkerank.funnystring import *
import unittest

class TestFunnyString(unittest.TestCase):
    def test_acxz_in_FunnyString(self):
        x = 'acxz'
        result = funnyString(x)
        self.assertEqual(result,'Funny')
    def test_bcxz_in_FunnyString(self):
        x = 'bcxz'
        result = funnyString(x)
        self.assertEqual(result,'Not Funny')
    def test_yrzxrxskrtlpwpmtpxvowrxrpxq_in_FunnyString(self):
        x = 'yrzxrxskrtlpwpmtpxvowrxrpxq'
        result = funnyString(x)
        self.assertEqual(result,'Not Funny')
    def test_jkmsxzwrxzy_in_FunnyString(self):
        x = 'jkmsxzwrxzy'
        result = funnyString(x)
        self.assertEqual(result,'Not Funny')
    def test_ivvkxq_in_FunnyString(self):
        x = 'ivvkxq'
        result = funnyString(x)
        self.assertEqual(result,'Not Funny')
if __name__ == '__main__':
    unittest.main()