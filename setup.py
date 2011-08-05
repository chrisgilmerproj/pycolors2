from distutils.core import setup

setup(
	name = 'pycolors2',
	py_modules = ['colors',],
	version = '0.0.2',
	author = 'Chris Gilmer',
	author_email = 'chris.gilmer@gmail.com',

	url = 'http://github.com/chrisgilmerproj/pycolors2',
	
	license = 'MIT license',
	description = """ Tool to color code python output """,

	long_description = open('README.markdown').read(),
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
