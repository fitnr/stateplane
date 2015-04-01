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
from stateplane import cli
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
        assert stateplane.from_latlon(40.2, -75.2) == (817080.8169336573, 99364.28495057777)

    def test_tolonlat(self):
        x, y = stateplane.to_lonlat(817080.8169336573, 99364.28495057777, epsg='32129')
        self.assertAlmostEqual(x, -75.2)
        self.assertAlmostEqual(y, 40.2)

        y, x = stateplane.to_latlon(817080.8169336573, 99364.28495057777, epsg='32129')
        self.assertAlmostEqual(x, -75.2)
        self.assertAlmostEqual(y, 40.2)

    def test_tolonlat_err(self):
        with self.assertRaises(ValueError):
            stateplane.to_latlon(817080.8169336573, 99364.28495057777)
            stateplane.to_lonlat(817080.8169336573, 99364.28495057777)

    def test_get_co(self):
        assert stateplane.stateplane._get_co('01001') == '26930'
        assert stateplane.stateplane._get_co('72123') == '32161'

    def test_identify_with_countyfp(self):
        assert 'NY_LI' == stateplane.identify(None, None, fmt='short', statefp='36', countyfp='005')
        assert 'NY_LI' == stateplane.identify(None, None, fmt='short', countyfp='36005')

    def test_identify(self):
        assert 'NY_LI' == stateplane.identify(-73.604107, 40.750638, fmt='short')
        assert 'NC' == stateplane.identify(-80.1, 36.2, fmt='short')
        assert '3200' == stateplane.identify(-80.1, 36.2, fmt='fips')
        assert stateplane.identify(-75.2, 40.2, fmt='short') == 'PA_S'
        assert stateplane.identify(-75.2, 40.2) == '32129'

        assert stateplane.identify(-80.1, 36.2, fmt='proj4') == "+proj=lcc +lat_1=36.16666666666666 +lat_2=34.33333333333334 +lat_0=33.75 +lon_0=-79 +x_0=609601.22 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs"

        self.assertEqual(stateplane.identify(-80.1, 36.2, fmt='FOOBAR'), '32119')


    def test_inverting(self):
        for _ in range(500):
            lon, lat = rand()
            epsg = stateplane.identify(lon, lat)
            e, n = stateplane.from_lonlat(lon, lat)
            x, y = stateplane.to_lonlat(e, n, epsg=epsg)
            self.assertAlmostEqual(lon, x)
            self.assertAlmostEqual(lat, y)

    def test_statefp(self):
        assert '26943' == stateplane.identify(-121.986361, 37.524384999999995, statefp='06')
        self.assertEqual('26957', stateplane.identify(0, 0, statefp='10'))
        self.assertRaises(ValueError, stateplane.identify, -121, 35.7, statefp='KK')

