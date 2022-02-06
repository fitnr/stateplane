# This file is part of stateplane.
# https://github.com/fitnr/stateplane

# Licensed under the GPLv3 license:
# http://http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

import json
import os.path
from csv import reader

import pyproj
from shapely.geometry import shape
from shapely.geometry.point import Point

from . import dicts

try:
    import importlib.resources as resources
except ImportError:
    import importlib_resources as resources


def _load_boundaries():
    with resources.open_binary('stateplane', 'stateplane.geojson') as f:
        geojson = json.load(f)
        for feature in geojson['features']:
            feature['geometry'] = shape(feature['geometry'])
            yield feature


def _cofips():
    with resources.open_text('stateplane', 'countyfp.csv') as rs:
        r = reader(rs, delimiter=",")
        next(r)
        return {fp: epsg for fp, epsg in r}


class Stateplane(object):

    """Stateplane class for doing many conversions"""

    def __init__(self):
        self.projections = dict()
        self.STATEPLANES = list(_load_boundaries())
        self.COFIPS = _cofips()

    def _get_co(self, countyfp, statefp=None):
        if statefp and len(countyfp) == 3:
            countyfp = statefp + countyfp

        try:
            return self.COFIPS[countyfp]
        except KeyError:
            # Guess the countyfp didn't work
            pass

    def _id(self, lon, lat, statefp=None, countyfp=None):
        stateplanes = None
        if countyfp:
            epsgmatch = self._get_co(countyfp, statefp)
            if epsgmatch:
                stateplanes = [s for s in self.STATEPLANES if s["properties"]["EPSG"] == epsgmatch]

        elif statefp:
            stateplanes = [s for s in self.STATEPLANES if s["properties"]["STATEFP"] == str(statefp)]

        else:
            stateplanes = self.STATEPLANES

        if not stateplanes:
            raise ValueError("SPCS not found for statefp={}".format(statefp))

        if len(stateplanes) == 1:
            return stateplanes[0]

        target = Point(lon, lat)
        result = None

        for stateplane in stateplanes:
            if stateplane["geometry"].contains(target):
                result = stateplane
                break

        if not result:
            stateplanes.sort(key=lambda x: x["geometry"].distance(target))
            result = stateplanes[0]

        return result

    def _convert(self, x, y, inverse, epsg=None, fips=None, abbr=None, statefp=None):
        """Conversion helper for state plane conversions"""
        if inverse and not any((epsg, fips, abbr)):
            raise ValueError("Inverse calculations require a epsg, fips or abbr argument.")

        if fips:
            epsg = dicts.FIPS_TO_EPSG[fips]
        elif abbr:
            epsg = dicts.SHORT_TO_EPSG[abbr]

        if not epsg:
            epsg = self.identify(x, y, statefp=statefp)

        if epsg not in self.projections:
            self.projections[epsg] = pyproj.Proj("EPSG:" + epsg)

        projection = self.projections[epsg]

        return projection(x, y, inverse=inverse)

    def identify(self, lon, lat, fmt=None, statefp=None, countyfp=None):
        """Return stateplane for given X, Y coordinates
        Returns a pyproj.CRS object
        Defaults to returning EPSG code. Other possible fmt parameters:
        - fips
        - short (e.g. 'NY_LI')
        """
        result = self._id(lon, lat, statefp=statefp, countyfp=countyfp)

        try:
            if fmt == "fips":
                return result["properties"]["FIPSZONE83"]

            if fmt == "short":
                return result["properties"]["ZONENAME83"]

            return result["properties"]["EPSG"]

        except TypeError:
            pass

    def from_latlon(self, lat, lon, epsg=None, fips=None, abbr=None, statefp=None):
        return self._convert(lon, lat, None, epsg, fips, abbr, statefp=statefp)

    def from_lonlat(self, lon, lat, epsg=None, fips=None, abbr=None, statefp=None):
        """Convert from (lon, lat) to local state plane coordinates"""
        return self._convert(lon, lat, None, epsg, fips, abbr, statefp=statefp)

    def to_latlon(self, easting, northing, epsg=None, fips=None, abbr=None):
        lon, lat = self.to_lonlat(easting, northing, epsg, fips, abbr)
        return lat, lon

    def to_lonlat(self, easting, northing, epsg=None, fips=None, abbr=None):
        """Return (lon, lat) from a state plane (easting, northing) pair.
        Must pass either a fips code, epsg, or abbr to specify the state plane projection to use
        """
        if not any((epsg, fips, abbr)):
            raise ValueError("to long/lat calculations require a epsg, fips or abbr argument.")
        return self._convert(easting, northing, True, epsg, fips, abbr)
