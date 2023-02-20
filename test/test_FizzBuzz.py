from src.FizzBuzz import * 
import unittest

class TestFizzBuzz(unittest.TestCase):

    def test_FizzBuzz(self):
        self.assertEqual(FizzBuzz(1), None)
        self.assertEqual(FizzBuzz(2), None)
        self.assertEqual(FizzBuzz(3), "Fizz")
        self.assertEqual(FizzBuzz(4), None)
        self.assertEqual(FizzBuzz(5), "Buzz")
        self.assertEqual(FizzBuzz(6), "Fizz")
        self.assertEqual(FizzBuzz(7), None)
        self.assertEqual(FizzBuzz(8), None)
        self.assertEqual(FizzBuzz(9), "Fizz")
        self.assertEqual(FizzBuzz(10), "Buzz")
        self.assertEqual(FizzBuzz(15), "FizzBuzz")
        self.assertEqual(FizzBuzz(30), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()