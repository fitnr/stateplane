#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of stateplane.
# https://github.com/someuser/somepackage

# Licensed under the GPLv3 license:
# http://http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

from __future__ import unicode_literals
import unittest
import stateplane
from random import uniform

def rand():
    return uniform(-116.593781, -82.316437), uniform(32.287133, 42.293564)

class TestCase(unittest.TestCase):

    def test_functions_exist(self):
        assert hasattr(stateplane, 'from_latlon')
        assert hasattr(stateplane, 'from_lonlat')
        assert hasattr(stateplane, 'to_latlon')
        assert hasattr(stateplane, 'to_lonlat')
        assert hasattr(stateplane, 'identify')

    def test_fromlatlon(self):
        assert stateplane.from_lonlat(-75.2, 40.2) == (817080.8169336573, 99364.28495057777)

    def test_tolonlat(self):
        x, y = stateplane.to_lonlat(817080.8169336573, 99364.28495057777, epsg='32129')
        self.assertAlmostEqual(x, -75.2)
        self.assertAlmostEqual(y, 40.2)

    def test_identify(self):
        assert 'NY_LI' == stateplane.identify(-73.604107, 40.750638, fmt='short')
        assert 'NC' == stateplane.identify(-80.1, 36.2, fmt='short')
        assert stateplane.identify(-75.2, 40.2, fmt='short') == 'PA_S'
        assert stateplane.identify(-75.2, 40.2) == '32129'

    def test_inverting(self):
        for _ in range(1000):
            lon, lat = rand()
            epsg = stateplane.identify(lon, lat)
            e, n = stateplane.from_lonlat(lon, lat)
            x, y = stateplane.to_lonlat(e, n, epsg=epsg)
            self.assertAlmostEqual(lon, x)
            self.assertAlmostEqual(lat, y)
