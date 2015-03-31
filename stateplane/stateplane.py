import os.path
import pyproj
from shapely.geometry.polygon import Polygon
from shapely.geometry.multipolygon import MultiPolygon
from shapely.geometry.point import Point
import fiona
from . import data

STATEPLANES = []

with fiona.open('/stateplane.geojson',
                vfs='zip://' + os.path.join(os.path.dirname(__file__), 'data/stateplane.zip')) as src:
    for f in src:
        if f['geometry']['type'] == 'MultiPolygon':
            f['geometry'] = MultiPolygon([Polygon(c[0], c[1:]) for c in f['geometry']['coordinates']])

        elif f['geometry']['type'] == 'Polygon':
            f['geometry'] = Polygon(f['geometry']['coordinates'][0], f['geometry']['coordinates'][1:])

        STATEPLANES.append(f)


def select(lon, lat, fmt=None):
    '''Return stateplane for given X, Y coordinates
    Defaults to returning EPSG code. Possible fmt parameters: fips, abbr (e.g. 'NY_LI')
    '''
    target = Point(lon, lat)

    for stateplane in STATEPLANES:
        if stateplane['geometry'].contains(target):
            result = stateplane
            break

    if not result:
        STATEPLANES.sort(key=lambda x: x['geometry'].distance(target))
        result = STATEPLANES[0]

    try:
        if fmt == 'fips':
            return result['properties']['FIPSZONE83']

        elif fmt == 'short':
            return result['properties']['ZONENAME83']

        elif fmt == 'proj4':
            return data.EPSG_TO_PROJ4[result['properties']['EPSG']]

        else:
            return result['properties']['EPSG']

    except NameError:
        pass


class Stateplane(object):

    """Stateplane class for doing many conversions"""

    def __init__(self):
        self.projections = dict()

    def _convert(self, x, y, inv, epsg=None, fips=None, abbr=None):
        '''Conversion helper for state plane conversions'''
        if not any(fips, epsg, abbr):
            raise ValueError("Need either a fips, epsg or abbr argument")

        if fips:
            epsg = data.FIPS_TO_EPSG[fips]
        elif abbr:
            epsg = data.SHORT_TO_EPSG[abbr]

        if not any(inv, epsg):
            epsg = select(x, y)

        if epsg not in self.projections:
            self.projections[epsg] = pyproj.Proj(init='EPSG:' + epsg)

        projection = self.projections[epsg]

        return projection(x, y, inv=inv)

    def from_latlon(self, lat, lon, epsg=None, fips=None, abbr=None):
        return self._convert(lon, lat, None, fips, epsg, abbr)

    def from_lonlat(self, lon, lat, epsg=None, fips=None, abbr=None):
        '''Convert from (lon, lat) to local state plane coordinates'''
        return self._convert(lon, lat, None, fips, epsg, abbr)

    def to_latlon(self, easting, northing, epsg=None, fips=None, abbr=None):
        lon, lat = self._convert(easting, northing, True, fips, epsg, abbr)
        return lat, lon

    def to_lonlat(self, easting, northing, epsg=None, fips=None, abbr=None):
        '''Return (lon, lat) from a state plane (easting, northing) pair.
        Must pass either a fips code, epsg, or abbr to specify the state plane projection to use
        '''
        return self._convert(easting, northing, True, fips, epsg, abbr)