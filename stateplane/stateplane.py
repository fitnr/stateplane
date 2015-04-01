import os.path
import pyproj
from shapely.geometry.polygon import Polygon
from shapely.geometry.multipolygon import MultiPolygon
from shapely.geometry.point import Point
import fiona
from . import data

STATEPLANES = []

with fiona.open('/', vfs='zip://' + os.path.join(os.path.dirname(__file__), 'data/stateplane.zip')) as src:
    for f in src:
        if f['geometry']['type'] == 'MultiPolygon':
            f['geometry'] = MultiPolygon([Polygon(c[0], c[1:]) for c in f['geometry']['coordinates']])

        elif f['geometry']['type'] == 'Polygon':
            f['geometry'] = Polygon(f['geometry']['coordinates'][0], f['geometry']['coordinates'][1:])

        STATEPLANES.append(f)


def _id(lon, lat, statefp=None):
    if statefp:
        stateplanes = [s for s in STATEPLANES if s['properties']['STATEFP'] == str(statefp)]

        if len(stateplanes) == 1:
            return stateplanes[0]

        elif len(stateplanes) == 0:
            raise ValueError("SPCS not found for statefp={}".format(statefp))

    else:
        stateplanes = STATEPLANES

    target = Point(lon, lat)
    result = None

    for stateplane in stateplanes:
        if stateplane['geometry'].contains(target):
            result = stateplane
            break

    if not result:
        stateplanes.sort(key=lambda x: x['geometry'].distance(target))
        result = stateplanes[0]

    return result


def identify(lon, lat, fmt=None, statefp=None):
    '''Return stateplane for given X, Y coordinates
    Defaults to returning EPSG code. Possible fmt parameters: fips, abbr (e.g. 'NY_LI')
    '''

    result = _id(lon, lat, statefp=statefp)

    try:
        if fmt == 'fips':
            return result['properties']['FIPSZONE83']

        elif fmt == 'short':
            return result['properties']['ZONENAME83']

        elif fmt == 'proj4':
            return data.EPSG_TO_PROJ4[result['properties']['EPSG']]

        else:
            return result['properties']['EPSG']

    except TypeError:
        pass


class Stateplane(object):

    """Stateplane class for doing many conversions"""

    def __init__(self):
        self.projections = dict()

    def _convert(self, x, y, inverse, epsg=None, fips=None, abbr=None, statefp=None):
        '''Conversion helper for state plane conversions'''
        if inverse and not any((epsg, fips, abbr)):
            raise ValueError("Inverse calculations require a epsg, fips or abbr argument.")

        if fips:
            epsg = data.FIPS_TO_EPSG[fips]
        elif abbr:
            epsg = data.SHORT_TO_EPSG[abbr]

        if not epsg:
            epsg = identify(x, y, statefp=statefp)

        if epsg not in self.projections:
            self.projections[epsg] = pyproj.Proj(init='EPSG:' + epsg)

        projection = self.projections[epsg]

        return projection(x, y, inverse=inverse)

    def from_latlon(self, lat, lon, epsg=None, fips=None, abbr=None, statefp=None):
        return self._convert(lon, lat, None, epsg, fips, abbr, statefp=statefp)

    def from_lonlat(self, lon, lat, epsg=None, fips=None, abbr=None, statefp=None):
        '''Convert from (lon, lat) to local state plane coordinates'''
        return self._convert(lon, lat, None, epsg, fips, abbr, statefp=statefp)

    def to_latlon(self, easting, northing, epsg=None, fips=None, abbr=None):
        if not any((epsg, fips, abbr)):
            raise ValueError("to long/lat calculations require a epsg, fips or abbr argument.")
        lon, lat = self._convert(easting, northing, True, epsg, fips, abbr)
        return lat, lon

    def to_lonlat(self, easting, northing, epsg=None, fips=None, abbr=None):
        '''Return (lon, lat) from a state plane (easting, northing) pair.
        Must pass either a fips code, epsg, or abbr to specify the state plane projection to use
        '''
        if not any((epsg, fips, abbr)):
            raise ValueError("to long/lat calculations require a epsg, fips or abbr argument.")
        return self._convert(easting, northing, True, epsg, fips, abbr)
