
import unittest

import colors

class TestColors(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_color_text(self):
        orig = 'This should be red'
        output = colors.red(orig)
        expected = '\x1b[0;31m{0}\x1b[0m'.format(orig)
        self.assertEqual(output, expected)
