#!/usr/bin/python

import os
import subprocess

__all__ = ['Colors']


class Colors(object):
    PYCOLORS2_HAS_COLORS = 'PYCOLORS2_HAS_COLORS'
    PYCOLORS2_DISABLE_COLORS = 'PYCOLORS2_DISABLE_COLORS'

    COLORS = {
        'reset_all': '\033[0m',
        'bright': '\033[1m',
        'dim': '\033[2m',
        'normal': '\033[22m',

        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[39m',

        'black_background': '\033[40m',
        'red_background': '\033[41m',
        'green_background': '\033[42m',
        'yellow_background': '\033[33m',
        'blue_background': '\033[33m',
        'magenta_background': '\033[45m',
        'cyan_background': '\033[46m',
        'white_background': '\033[47m',
        'reset_background': '\033[49m',
    }

    def __init__(self):
        """ Checks if the shell supports colors """

        try:
            p = subprocess.Popen(['tput', 'colors'],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            num_colors = int(p.stdout.read())
        except (OSError, ValueError):
            num_colors = 1

        if num_colors > 1:
            os.environ[self.PYCOLORS2_HAS_COLORS] = '1'

        self.enable_colors()

    def enable_colors(self):
        """ Method to enable colors """
        if self.PYCOLORS2_DISABLE_COLORS in os.environ:
            del os.environ[self.PYCOLORS2_DISABLE_COLORS]

    def disable_colors(self):
        """ Method to disable colors """
        os.environ[self.PYCOLORS2_DISABLE_COLORS] = '1'

    def _wrap_color(self, code, text, format=None, style=None):
        """ Colors text with code and given format """
        if int(code) not in list(range(30, 38)) + [39]:
            raise Exception('Color code must be 30 - 37 and 39')

        if format == 'bold':
            code = "1;{0}".format(code)
        elif format == 'underline':
            code = "4;{0}".format(code)
        elif format == 'background':
            code = str(int(code) + 10)
        else:
            code = "0;{0}".format(code)
        if self.PYCOLORS2_HAS_COLORS in os.environ and \
           self.PYCOLORS2_DISABLE_COLORS not in os.environ:
            st = ''
            if style:
                st = self.COLORS.get(style, '')
            return "{0}\033[{1}m{2}\033[0m".format(st, code, text)
        else:
            return text

    def black(self, text, format=None):
        return self._wrap_color('30', text, format=format)

    def red(self, text, format=None):
        return self._wrap_color('31', text, format=format)

    def green(self, text, format=None):
        return self._wrap_color('32', text, format=format)

    def yellow(self, text, format=None):
        return self._wrap_color('33', text, format=format)

    def blue(self, text, format=None):
        return self._wrap_color('34', text, format=format)

    def magenta(self, text, format=None):
        return self._wrap_color('35', text, format=format)

    def cyan(self, text, format=None):
        return self._wrap_color('36', text, format=format)

    def white(self, text, format=None):
        return self._wrap_color('37', text, format=format)

    def reset(self, text, format=None):
        return self._wrap_color('39', text, format=format)
