=========
PyColors2
=========

This is a set of color methods and a dictionary that help you wrap 
text output in colors.  This tool was originally forked from the
Fabric fabric.colors library and upgraded with utilities from the
original pycolors tool in pypi.

Methods
=======

Using the methods is easy.  To make red text::
    
    from colors import *
    print(red('This will be red text'))

To mix text simply::

    from colors import *
    print(red('This will be red text') + green('and this will be green text.'))

Dictionary
==========

Similarly the dictionary can be used::

    from colors import *
    print('%(red)sThis will be red text %(green)sand this will be green text.%(normal)s' % COLORS)

