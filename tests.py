#!/usr/bin/python

import os
import sys
import unittest

# Third party apps
import mock

# This app
import colors

# One test doesn't work right in python 2.6
py26 = False
if sys.version_info < (2, 7):
    py26 = True


class TestColors(unittest.TestCase):

    def setUp(self):
        self.patcher = mock.patch('subprocess.Popen')
        self.subprocess = self.patcher.start()
        self.p = mock.Mock()
        self.p.stdout.read.return_value = '8'
        self.subprocess.return_value = self.p
        self.colors = colors.Colors()
        self.assertTrue(self.colors.PYCOLORS2_HAS_COLORS in os.environ)

    def tearDown(self):
        self.patcher.stop()
        if self.colors.PYCOLORS2_HAS_COLORS in os.environ:
            del os.environ[self.colors.PYCOLORS2_HAS_COLORS]
        if self.colors.PYCOLORS2_DISABLE_COLORS in os.environ:
            del os.environ[self.colors.PYCOLORS2_DISABLE_COLORS]

    def test_color_text(self):
        output = self.colors.red('This will be red text')
        expected = '\x1b[0;31mThis will be red text\x1b[0m'
        self.assertEqual(output, expected)

    def test_two_colors_text(self):
        output = self.colors.red('This will be red text') + \
            self.colors.green('and this will be green text.')
        expected = '\x1b[0;31mThis will be red text\x1b[0m\x1b[0;32m' \
                   'and this will be green text.\x1b[0m'
        self.assertEqual(output, expected)

    def test_colors_from_dictionary(self):
        output = '{red}This will be red text {green}' \
                 'and this will be green text.{normal}'.format(**self.colors.COLORS)
        expected = '\x1b[31mThis will be red text \x1b[32m' \
                   'and this will be green text.\x1b[0m'
        self.assertEqual(output, expected)

    def test_colors_format_bold(self):
        output = self.colors.red('This will be BOLD red text',
                            format='bold')
        expected = '\x1b[1;31mThis will be BOLD red text\x1b[0m'
        self.assertEqual(output, expected)

    def test_colors_format_underline(self):
        output = self.colors.red('This will be UNDERLINE red text',
                            format='underline')
        expected = '\x1b[4;31mThis will be UNDERLINE red text\x1b[0m'
        self.assertEqual(output, expected)

    def test_colors_format_background(self):
        output = self.colors.red('This will be BACKGROUND red text',
                            format='background')
        expected = '\x1b[41mThis will be BACKGROUND red text\x1b[0m'
        self.assertEqual(output, expected)

    def test_disable_colors(self):
        self.colors.enable_colors()
        self.assertTrue(self.colors.PYCOLORS2_DISABLE_COLORS not in os.environ)
        output = self.colors.red('This will be red text')
        expected = '\x1b[0;31mThis will be red text\x1b[0m'
        self.assertEqual(output, expected)
        self.colors.disable_colors()
        self.assertTrue(self.colors.PYCOLORS2_DISABLE_COLORS in os.environ)
        output = self.colors.red('This will be red text')
        expected = 'This will be red text'
        self.assertEqual(output, expected)

    def test_enable_colors(self):
        self.colors.disable_colors()
        self.assertTrue(self.colors.PYCOLORS2_DISABLE_COLORS in os.environ)
        output = self.colors.red('This will be red text')
        expected = 'This will be red text'
        self.assertEqual(output, expected)
        self.colors.enable_colors()
        self.assertTrue(self.colors.PYCOLORS2_DISABLE_COLORS not in os.environ)
        output = self.colors.red('This will be red text')
        expected = '\x1b[0;31mThis will be red text\x1b[0m'
        self.assertEqual(output, expected)

    def test_wrap_colors_bad_code(self):
        if py26:
            self.assertRaises(Exception, self.colors._wrap_color, '38', 'This should fail')
        else:
            with self.assertRaises(Exception) as cm:
                self.colors._wrap_color('38', 'This should fail')
            e = cm.exception
            self.assertEqual(str(e), 'Color code must be 30 - 37')


class TestColorsUnavailable(unittest.TestCase):

    def setUp(self):
        self.patcher = mock.patch('subprocess.Popen')
        self.subprocess = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        c = colors.Colors()
        if c.PYCOLORS2_HAS_COLORS in os.environ:
            del os.environ[c.PYCOLORS2_HAS_COLORS]
        if c.PYCOLORS2_DISABLE_COLORS in os.environ:
            del os.environ[c.PYCOLORS2_DISABLE_COLORS]

    def test_colors_not_available(self):
        self.p = mock.Mock()
        self.p.stdout.read.return_value = '1'
        self.subprocess.return_value = self.p
        c = colors.Colors()
        self.assertTrue(c.PYCOLORS2_HAS_COLORS not in os.environ)
        output = c.red('This will be red text')
        expected = 'This will be red text'
        self.assertEqual(output, expected)

    def test_colors_not_available_oserror(self):
        self.p = mock.Mock()
        self.p.stdout.read.side_effect = OSError
        self.subprocess.return_value = self.p
        c = colors.Colors()
        self.assertTrue(c.PYCOLORS2_HAS_COLORS not in os.environ)
        output = c.red('This will be red text')
        expected = 'This will be red text'
        self.assertEqual(output, expected)

    def test_colors_not_available_valueerror(self):
        self.p = mock.Mock()
        self.p.stdout.read.side_effect = ValueError
        self.subprocess.return_value = self.p
        c = colors.Colors()
        self.assertTrue(c.PYCOLORS2_HAS_COLORS not in os.environ)
        output = c.red('This will be red text')
        expected = 'This will be red text'
        self.assertEqual(output, expected)


def run_tests(test_names=None, test_class_list=None, module=None, verbose=2):
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    if test_names:
        tests = loader.loadTestsFromNames(test_names, module=module)
        suite.addTests(tests)
    else:
        if not test_class_list:
            return
        for test_class in test_class_list:
            tests = loader.loadTestsFromTestCase(test_class)
            suite.addTests(tests)
    unittest.TextTestRunner(verbosity=verbose).run(suite)


if __name__ == '__main__':
    test_class_list = [TestColors, TestColorsUnavailable]
    run_tests(test_names=sys.argv[1:],
              test_class_list=test_class_list,
              module=sys.modules[__name__])
