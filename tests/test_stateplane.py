# -*- coding: utf-8 -*-

# This file is part of stateplane.
# https://github.com/fitnr/stateplane

# Licensed under the GPLv3 license:
# http://http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

from __future__ import unicode_literals
import unittest
from random import uniform
import pyproj
import stateplane
from stateplane import dicts
from stateplane.stateplane import Stateplane


def rand():
    return uniform(-116.593781, -82.316437), uniform(32.287133, 42.293564)


class TestCase(unittest.TestCase):

    easting = 817080.8169336562
    northing = 99364.28495058486

    def setUp(self):
        self.sp = Stateplane()

    def assertSequenceAlmostEqual(self, seq1, seq2, *args):
        self.assertEqual(len(seq1), len(seq2))
        for i, (a, b) in enumerate(zip(seq1, seq2)):
            try:
                self.assertAlmostEqual(a, b, *args)
            except AssertionError as e:
                msg = f"Sequences differ: {seq1} != {seq2}\n\nFirst differing element {i}:\n{a}\n{b}"
                raise self.failureException(msg) from e

    def test_functions_exist(self):
        assert hasattr(stateplane, 'from_latlon')
        assert hasattr(stateplane, 'from_lonlat')
        assert hasattr(stateplane, 'to_latlon')
        assert hasattr(stateplane, 'to_lonlat')
        assert hasattr(stateplane, 'identify')

    def test_raw(self):
        t0 = pyproj.Transformer.from_crs(32129, 4326)
        sp_coords = t0.transform(40.2, -75.2, direction=pyproj.enums.TransformDirection.INVERSE)
        self.assertSequenceEqual(sp_coords, (self.easting, self.northing))
        lonlat_coords = t0.transform(*sp_coords)
        self.assertSequenceAlmostEqual((40.2, -75.2), lonlat_coords)
        t1 = self.sp.get_transformer(-75.2, 40.2)
        self.assertEqual(t1, t0)

    def test_fromlonlat(self):
        result = self.sp.from_lonlat(-75.2, 40.2)
        fixture = (self.easting, self.northing)
        self.assertSequenceAlmostEqual(result, fixture, 5)

    def test_fromlatlon(self):
        result = stateplane.from_latlon(40.2, -75.2)
        fixture = (self.easting, self.northing)
        self.assertSequenceAlmostEqual(result, fixture, 5)

    def test_gettransformer(self):
        t = self.sp.get_transformer(self.easting, self.northing, epsg=32129)
        self.assertEqual(t, pyproj.Transformer.from_crs(pyproj.CRS(32129), 4326))

    def test_tolonlat(self):
        result = self.sp.to_lonlat(self.easting, self.northing, epsg='32129')
        self.assertSequenceAlmostEqual(result, (-75.2, 40.2))

    def test_tolatlon(self):
        result = self.sp.to_latlon(self.easting, self.northing, epsg='32129')
        self.assertSequenceAlmostEqual(result, (40.2, -75.2))

    def test_tolatlon_err(self):
        with self.assertRaises(ValueError):
            self.sp.to_latlon(self.easting, self.northing)

    def test_tolonlat_err(self):
        with self.assertRaises(ValueError):
            self.sp.to_lonlat(self.easting, self.northing)

    def test_get_co(self):
        """Spot check counties"""
        self.assertEqual(self.sp._get_co('01001'), '26930')
        self.assertEqual(self.sp._get_co('72123'), '32161')
        self.assertEqual(self.sp._get_co("46102"), "32135")
        self.assertEqual(dicts.STATEFP_TO_EPSG["46"], ("32135", "32134"))

    def test_identify_with_countyfp(self):
        self.assertEqual('NY_LI', stateplane.identify(None, None, fmt='short', statefp='36', countyfp='005'))
        self.assertEqual('NY_LI', stateplane.identify(None, None, fmt='short', countyfp='36005'))

    def test_identify(self):
        self.assertEqual('NY_LI', stateplane.identify(-73.604107, 40.750638, fmt='short'))
        self.assertEqual('NC', stateplane.identify(-80.1, 36.2, fmt='short'))
        self.assertEqual('3200', stateplane.identify(-80.1, 36.2, fmt='fips'))
        self.assertEqual(stateplane.identify(-75.2, 40.2, fmt='short'), 'PA_S')
        self.assertEqual(stateplane.identify(-75.2, 40.2), '32129')
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
        self.assertEqual('26943', stateplane.identify(-121.986361, 37.524384999999995, statefp='06'))
        self.assertEqual('26957', stateplane.identify(0, 0, statefp='10'))
        self.assertRaises(ValueError, stateplane.identify, -121, 35.7, statefp='KK')

if __name__ == '__main__':
    unittest.main()
