from distutils.core import setup

setup(
	name = 'pycolors2',
	packages = ['colors',],
	version = 'v0.0.1',
	author = 'RED Interactive Agency',
	author_email = 'geeks@ff0000.com',

	url = 'http://www.github.com/ff0000/colors/',
	download_url = 'http://www.github.com/ff0000/colors/',
	
	license = 'MIT license',
	description = """ Tool to color code python output """,

	long_description = open('README.rst').read(),
	requires = [],

	classifiers = (
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Programming Language :: Python',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: System',
		'Topic :: Terminals',
		'Topic :: Utilities',
	),
)
