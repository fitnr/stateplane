#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of stateplane.
# https://github.com/someuser/somepackage

# Licensed under the GPLv3 license:
# http://http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

from setuptools import setup, find_packages

try:
    readme = open('readme.rst').read()
except IOError:
    readme = open('readme.md').read()

setup(
    name='stateplane',
    version='0.2.2',
    description='Convert between state plane projections and long/lat',
    long_description=readme,
    keywords='gis usa projection',
    author='Neil Freeman',
    author_email='contact@fakeisthenewreal.org',
    url='https://github.com/fitnr/stateplane',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,

    package_data={
        'stateplane': ['data/*.zip', 'data/*.csv']
    },

    install_requires=[
        'fiona>=1.4.8,<1.6',
        'pyproj>=1.9.4,<2',
        'shapely>=1.5.1,<1.6',
    ],
    test_suite='tests',

    entry_points={
        'console_scripts': [
            'stateplane=stateplane.cli:main',
        ],
    },
    zip_safe=False,
)
