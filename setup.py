#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of stateplane.
# https://github.com/fitnr/stateplane

# Licensed under the GPLv3 license:
# http://http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

from setuptools import setup, find_packages

try:
    readme = open('README.md').read()
except IOError:
    readme = ''

setup(
    name='stateplane',
    version='0.4.0',
    description='Convert between state plane projections and long/lat',
    long_description=readme,
    long_description_content_type='text/markdown',
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,

    package_data={
        'stateplane': ['data/*.zip', 'data/*.csv']
    },

    install_requires=[
        'pyproj>=2.4.2',
        'shapely',
        'GDAL',
    ],
    test_suite='tests',

    entry_points={
        'console_scripts': [
            'stateplane=stateplane.cli:main',
        ],
    },
    zip_safe=False,
)
