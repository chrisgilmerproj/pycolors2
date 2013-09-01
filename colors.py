#!/usr/bin/env python

import os
import subprocess

__all__ = ['Colors']


class Colors(object):
    PYCOLORS2_HAS_COLORS = 'PYCOLORS2_HAS_COLORS'
    PYCOLORS2_DISABLE_COLORS = 'PYCOLORS2_DISABLE_COLORS'

    COLORS = {
        'normal': '\033[0m',
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
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

    def _wrap_color(self, code):
        def inner(text, format=None):
            c = code
            if format == 'bold':
                c = "1;%s" % c
            elif format == 'underline':
                c = "4;%s" % c
            elif format == 'background':
                c = "%s" % str(int(c)+10)
            else:
                c = "0;%s" % c
            if self.PYCOLORS2_HAS_COLORS in os.environ and \
               self.PYCOLORS2_DISABLE_COLORS not in os.environ:
                return "\033[%sm%s\033[0m" % (c, text)
            else:
                return text
        inner.__doc__ = 'Colors text with code %s and given format' % (code)
        return inner

    def black(self, text, format=None):
        return self._wrap_color('30')(text, format=format)

    def red(self, text, format=None):
        return self._wrap_color('31')(text, format=format)

    def green(self, text, format=None):
        return self._wrap_color('32')(text, format=format)

    def yellow(self, text, format=None):
        return self._wrap_color('33')(text, format=format)

    def blue(self, text, format=None):
        return self._wrap_color('34')(text, format=format)

    def magenta(self, text, format=None):
        return self._wrap_color('35')(text, format=format)

    def cyan(self, text, format=None):
        return self._wrap_color('36')(text, format=format)

    def white(self, text, format=None):
        return self._wrap_color('37')(text, format=format)
