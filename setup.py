from distutils.core import setup

setup(
    name = 'pycolors2',
    py_modules = ['colors',],
    version = '0.0.4',
    author = 'Chris Gilmer',
    author_email = 'chris.gilmer@gmail.com',
    maintainer = 'Chris Gilmer',
    maintainer_email = 'chris.gilmer@gmail.com',

    url = 'http://github.com/chrisgilmerproj/pycolors2',

    license = 'MIT license',
    description = """ Tool to color code python output """,

    long_description = open('README.markdown').read(),
    requires = [],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)
