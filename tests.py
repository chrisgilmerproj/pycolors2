
import unittest

import colors


class TestColors(unittest.TestCase):

    def tearDown(self):
        colors.enable_colors()

    def test_color_text(self):
        output = colors.red('This will be red text')
        expected = '\x1b[0;31mThis will be red text\x1b[0m'
        self.assertEqual(output, expected)

    def test_two_colors_text(self):
        output = colors.red('This will be red text') + \
            colors.green('and this will be green text.')
        expected = '\x1b[0;31mThis will be red text\x1b[0m\x1b[0;32m' \
                   'and this will be green text.\x1b[0m'
        self.assertEqual(output, expected)

    def test_colors_from_dictionary(self):
        output = '{red}This will be red text {green}' \
                 'and this will be green text.{normal}'.format(**colors.COLORS)
        expected = '\x1b[31mThis will be red text \x1b[32m' \
                   'and this will be green text.\x1b[0m'
        self.assertEqual(output, expected)

    def test_colors_format_bold(self):
        output = colors.red('This will be BOLD red text',
                            format='bold')
        expected = '\x1b[1;31mThis will be BOLD red text\x1b[0m'
        self.assertEqual(output, expected)

    def test_colors_format_underline(self):
        output = colors.red('This will be UNDERLINE red text',
                            format='underline')
        expected = '\x1b[4;31mThis will be UNDERLINE red text\x1b[0m'
        self.assertEqual(output, expected)

    def test_colors_format_background(self):
        output = colors.red('This will be BACKGROUND red text',
                            format='background')
        expected = '\x1b[41mThis will be BACKGROUND red text\x1b[0m'
        self.assertEqual(output, expected)

    def test_disable_colors(self):
        output = colors.red('This will be red text')
        expected = '\x1b[0;31mThis will be red text\x1b[0m'
        self.assertEqual(output, expected)
        colors.disable_colors()
        output = colors.red('This will be red text')
        expected = 'This will be red text'
        self.assertEqual(output, expected)

    def test_enable_colors(self):
        colors.disable_colors()
        output = colors.red('This will be red text')
        expected = 'This will be red text'
        self.assertEqual(output, expected)
        colors.enable_colors()
        output = colors.red('This will be red text')
        expected = '\x1b[0;31mThis will be red text\x1b[0m'
        self.assertEqual(output, expected)
