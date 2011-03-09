#!/usr/bin/env python

from os import environ
from subprocess import Popen, PIPE

__all__ = [
	# Methods
	'enable_colors','disable_colors',

	# Dictionary of color codes
	'COLORS',
	
	# Color methods
	'black','red','green','yellow','blue','magenta','cyan','white'
]

def __has_colors():
	""" Checks if the shell supports colors """

	p = Popen('tput colors', stdout=PIPE, stderr=PIPE, shell=True)

	try:
		num_colors = int(p.stdout.read())
	except:
		num_colors = 1
	
	if num_colors > 1:
		environ['HASCOLORS'] = '1'

def enable_colors():
	""" Method to enable colors """
	del environ['DISABLE_COLORS']

def disable_colors():
	""" Method to disable colors """
	environ['DISABLE_COLORS'] = '1'

__has_colors()

COLORS = dict(
	normal  = '\033[0m',
	black   = '\033[30m',
	red     = '\033[31m',
	green   = '\033[32m',
	yellow  = '\033[33m',
	blue    = '\033[34m',
	magenta = '\033[35m',
	cyan    = '\033[36m',
	white   = '\033[37m',
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
		if 'HASCOLORS' in environ and 'DISABLE_COLORS' not in environ:
			return "\033[%sm%s\033[0m" % (c, text) 
		else:
			return text
	inner.__doc__ = 'Colors text with code %s and given format' % (code)
	return inner

black   = _wrap_color('30')
red     = _wrap_color('31')
green   = _wrap_color('32')
yellow  = _wrap_color('33')      
blue    = _wrap_color('34')        
magenta = _wrap_color('35')     
cyan    = _wrap_color('36')        
white   = _wrap_color('37')

