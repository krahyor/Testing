from src.hackkerank.gridChallenge import *
import unittest

class TestGridChallenge(unittest.TestCase):
    def test_gridChallenge(self):
        # Test case 1
        grid = [
            'abc',
            'def',
            'ghi'
        ]
        self.assertEqual(gridChallenge(grid), 'YES')

        # Test case 2
        grid = [
            'ebacd',
            'fghij',
            'olmkn',
            'trpqs',
            'xywuv'
        ]
        self.assertEqual(gridChallenge(grid), 'YES')

        # Test case 3
        grid = [
            'mpxz',
            'abcd',
            'wlmf'
        ]
        self.assertEqual(gridChallenge(grid), 'NO')

if __name__ == '__main__':
    unittest.main()