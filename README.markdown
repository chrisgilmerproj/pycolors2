# PyColors2

This is a set of color methods and a dictionary that help you wrap 
text output in colors.  This tool was originally forked from the
Fabric fabric.colors library and upgraded with utilities from the
original pycolors tool in pypi.

Maintainer: Chris Gilmer

[![Build Status](https://travis-ci.org/chrisgilmerproj/pycolors2.png)](https://travis-ci.org/chrisgilmerproj/pycolors2)
[PyColors2 ReadTheDocs](https://readthedocs.org/projects/pycolors2/)

## Methods

Using the methods is easy.  To make red text:
    
    import colors
    c = colors.Colors()
    print(c.red('This will be red text'))

To mix text simply:

    import colors
    c = colors.Colors()
    print(c.red('This will be red text') + c.green('and this will be green text.'))

## Dictionary

Similarly the dictionary can be used:

    import colors
    c = colors.Colors()
    print('{red}This will be red text {green}and this will be green text.{normal}'.format(**c.COLORS))

## Formatting

There are also several formats you can use when printing your code:

    import colors
    c = colors.Colors()
    print(c.red('This will be BOLD red text', format='bold'))
    print(c.red('This will be UNDERLINE red text', format='underline'))
    print(c.red('This will be BACKGROUND red text', format='background'))

## Environment

You can enable or disable the colors in your program at any time:

    import colors
    c = colors.Colors()
    print(c.red('This will be red text'))
    c.disable_colors()
    print(c.red('This will not be red text because colors are disabled'))
    c.enable_colors()
    print(c.red('This will be red text now that colors are enabled'))

Note that this will not work with the dictionary method, only with the actual
color methods.

## API Changes from 0.0.2 to latest

Older versions of pycolors2 allowed you to do the following:

    from colors import *
    print(red('This will be red text'))

This was deprecated in favor of being more pythonic:

    import colors
    c = colors.Colors()
    print(c.red('This will be red text'))

However, you may not want to have to update everything so you can use this:

    import colors
    c = colors.Colors()
    red = c.red
    print(red('This will be red text'))

It's nearly the same and it will keep you from having to refactor a lot of
your code.
