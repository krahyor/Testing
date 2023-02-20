from src.draw_staircase import *
import io
import unittest
from contextlib import redirect_stdout

class TestDrawStaircase(unittest.TestCase):

    def test_draw_staircase(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            draw_staircase(3, "*")
            output = buf.getvalue()
            expected_output = "*\n**\n***\n"
            self.assertEqual(output, expected_output)

        with io.StringIO() as buf, redirect_stdout(buf):
            draw_staircase(5, "#")
            output = buf.getvalue()
            expected_output = "#\n##\n###\n####\n#####\n"
            self.assertEqual(output, expected_output)

        with io.StringIO() as buf, redirect_stdout(buf):
            draw_staircase(1, "@")
            output = buf.getvalue()
            expected_output = "@\n"
            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()