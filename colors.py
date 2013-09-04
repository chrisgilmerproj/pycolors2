#!/usr/bin/python

import subprocess

__all__ = ['Colors']


class ANSIColors(object):
    ESCAPE = '\033['
    TRAIL = 'm'
    PREFIX = ''

    @classmethod
    def get_color(cls, color):
        code = cls.COLORS.get(color, None)
        if None:
            return ''
        return '{0}{1}{2}'.format(cls.ESCAPE, code, cls.TRAIL)

    @classmethod
    def get_all(cls):
        return sorted([cls.get_color(key) for key in cls.COLORS])

    @classmethod
    def get_dict(cls):
        colors = {}
        for key in cls.COLORS:
            colors['{0}{1}'.format(cls.PREFIX, key)] = cls.get_color(key)
        return colors


class ForegroundColors(ANSIColors):
    COLORS = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
        'reset': '39',
    }


class BackgroundColors(ANSIColors):
    PREFIX = 'bg_'
    COLORS = {
        'black': '40',
        'red': '41',
        'green': '42',
        'yellow': '43',
        'blue': '44',
        'magenta': '45',
        'cyan': '46',
        'white': '47',
        'reset': '49',
    }


class StyleColors(ANSIColors):
    COLORS = {
        'reset_all': '0',
        'bright': '1',
        'dim': '2',
        'normal': '22',
    }


class Colors(object):

    def __init__(self):
        """ Checks if the shell supports colors """

        try:
            p = subprocess.Popen(['tput', 'colors'],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            num_colors = int(p.stdout.read())
        except (OSError, ValueError):
            num_colors = 1

        self.has_colors = False
        if num_colors > 1:
            self.has_colors = True

        self.enable_colors()

        self.COLORS = self.enumerate_colors()

    def enumerate_colors(self):
        colors = {}
        cls_list = [ForegroundColors,
                    BackgroundColors,
                    StyleColors]
        for cls in cls_list:
            colors.update(cls.get_dict())
        return colors

    def enable_colors(self):
        """ Method to enable colors """
        self.colors_enabled = True

    def disable_colors(self):
        """ Method to disable colors """
        self.colors_enabled = False

    def _wrap_color(self, code, text, format=None, style=None):
        """ Colors text with code and given format """
        color = self.COLORS.get(code, None)
        if not color:
            raise Exception('Color code not found')

        if format and format not in ['bold', 'underline']:
            raise Exception('Color format not found')

        fmt = "0;"
        if format == 'bold':
            fmt = "1;"
        elif format == 'underline':
            fmt = "4;"

        # Manage the format
        parts = color.split('[')
        color = '{0}[{1}{2}'.format(parts[0], fmt, parts[1])

        if self.has_colors and self.colors_enabled:
            # Set brightness
            st = ''
            if style:
                st = self.COLORS.get(style, '')
            return "{0}{1}{2}{3}".format(st, color, text, self.COLORS['reset_all'])
        else:
            return text

    # Foreground
    def black(self, text, format=None, style=None):
        return self._wrap_color('black', text, format=format, style=style)

    def red(self, text, format=None, style=None):
        return self._wrap_color('red', text, format=format, style=style)

    def green(self, text, format=None, style=None):
        return self._wrap_color('green', text, format=format, style=style)

    def yellow(self, text, format=None, style=None):
        return self._wrap_color('yellow', text, format=format, style=style)

    def blue(self, text, format=None, style=None):
        return self._wrap_color('blue', text, format=format, style=style)

    def magenta(self, text, format=None, style=None):
        return self._wrap_color('magenta', text, format=format, style=style)

    def cyan(self, text, format=None, style=None):
        return self._wrap_color('cyan', text, format=format, style=style)

    def white(self, text, format=None, style=None):
        return self._wrap_color('white', text, format=format, style=style)

    def reset(self, text, format=None, style=None):
        return self._wrap_color('reset', text, format=format, style=style)

    # Background
    def bg_black(self, text, format=None, style=None):
        return self._wrap_color('bg_black', text, format=format, style=style)

    def bg_red(self, text, format=None, style=None):
        return self._wrap_color('bg_red', text, format=format, style=style)

    def bg_green(self, text, format=None, style=None):
        return self._wrap_color('bg_green', text, format=format, style=style)

    def bg_yellow(self, text, format=None, style=None):
        return self._wrap_color('bg_yellow', text, format=format, style=style)

    def bg_blue(self, text, format=None, style=None):
        return self._wrap_color('bg_blue', text, format=format, style=style)

    def bg_magenta(self, text, format=None, style=None):
        return self._wrap_color('bg_magenta', text, format=format, style=style)

    def bg_cyan(self, text, format=None, style=None):
        return self._wrap_color('bg_cyan', text, format=format, style=style)

    def bg_white(self, text, format=None, style=None):
        return self._wrap_color('bg_white', text, format=format, style=style)

    def bg_reset(self, text, format=None, style=None):
        return self._wrap_color('bg_reset', text, format=format, style=style)
