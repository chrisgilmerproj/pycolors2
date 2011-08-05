# PyColors2

This is a set of color methods and a dictionary that help you wrap 
text output in colors.  This tool was originally forked from the
Fabric fabric.colors library and upgraded with utilities from the
original pycolors tool in pypi.

Maintainer: Chris Gilmer

## Methods

Using the methods is easy.  To make red text::
    
    from colors import *
    print(red('This will be red text'))

To mix text simply::

    from colors import *
    print(red('This will be red text') + green('and this will be green text.'))

## Dictionary

Similarly the dictionary can be used::

    from colors import *
    print('%(red)sThis will be red text %(green)sand this will be green text.%(normal)s' % COLORS)

## Formatting

There are also several formats you can use when printing your code:

    from colors import *
    print(red('This will be BOLD red text', format='bold'))
    print(red('This will be UNDERLINE red text', format='underline'))
    print(red('This will be BACKGROUND red text', format='background'))

## Environment

You can enable or disable the colors in your program at any time:

    from colors import *
    print(red('This will be red text'))
    disable_colors()
    print(red('This will not be red text because colors are disabled'))
    enable_colors()
    print(red('This will be red text now that colors are enabled'))

