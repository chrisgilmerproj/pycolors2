#!/usr/bin/env python

import os
import subprocess

__all__ = [
    # Methods
    'enable_colors', 'disable_colors',
    # Dictionary of color codes
    'COLORS',
    # Color methods
    'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
]


COLORS_HAS_KEY = 'HAS_COLORS'
COLORS_DISABLE_KEY = 'DISABLE_COLORS'


def __has_colors():
    """ Checks if the shell supports colors """

    p = subprocess.Popen(['tput', 'colors'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    try:
        num_colors = int(p.stdout.read())
    except:
        num_colors = 1

    if num_colors > 1:
        os.environ[COLORS_HAS_KEY] = '1'


def enable_colors():
    """ Method to enable colors """
    if COLORS_DISABLE_KEY in os.environ:
        del os.environ[COLORS_DISABLE_KEY]


def disable_colors():
    """ Method to disable colors """
    os.environ[COLORS_DISABLE_KEY] = '1'

__has_colors()

COLORS = dict(
    normal='\033[0m',
    black='\033[30m',
    red='\033[31m',
    green='\033[32m',
    yellow='\033[33m',
    blue='\033[34m',
    magenta='\033[35m',
    cyan='\033[36m',
    white='\033[37m',
)


def _wrap_color(code):
    def inner(text, format=''):
        c = code
        if format == 'bold':
            c = "1;%s" % c
        elif format == 'underline':
            c = "4;%s" % c
        elif format == 'background':
            c = "%s" % str(int(c)+10)
        else:
            c = "0;%s" % c
        if COLORS_HAS_KEY in os.environ and \
           COLORS_DISABLE_KEY not in os.environ:
            return "\033[%sm%s\033[0m" % (c, text)
        else:
            return text
    inner.__doc__ = 'Colors text with code %s and given format' % (code)
    return inner

black = _wrap_color('30')
red = _wrap_color('31')
green = _wrap_color('32')
yellow = _wrap_color('33')
blue = _wrap_color('34')
magenta = _wrap_color('35')
cyan = _wrap_color('36')
white = _wrap_color('37')
