# PyColors2

This is a set of color methods and a dictionary that help you wrap 
text output in colors.  This tool was originally forked from the
Fabric fabric.colors library and upgraded with utilities from the
original pycolors tool in pypi.

Maintainer: Chris Gilmer

[![Build Status](https://travis-ci.org/chrisgilmerproj/pycolors2.png)](https://travis-ci.org/chrisgilmerproj/pycolors2)

## Methods

Using the methods is easy.  To make red text::
    
    import colors
    print(colors.red('This will be red text'))

To mix text simply::

    import colors
    print(colors.red('This will be red text') + colors.green('and this will be green text.'))

## Dictionary

Similarly the dictionary can be used::

    import colors
    print('{red}This will be red text {green}and this will be green text.{normal}'.format(**colors.COLORS))

## Formatting

There are also several formats you can use when printing your code:

    import colors
    print(colors.red('This will be BOLD red text', format='bold'))
    print(colors.red('This will be UNDERLINE red text', format='underline'))
    print(colors.red('This will be BACKGROUND red text', format='background'))

## Environment

You can enable or disable the colors in your program at any time:

    import colors
    print(colors.red('This will be red text'))
    colors.disable_colors()
    print(colors.red('This will not be red text because colors are disabled'))
    colors.enable_colors()
    print(colors.red('This will be red text now that colors are enabled'))

Note that this will not work with the dictionary method, only with the actual
color methods.
