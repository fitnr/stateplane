import os.path
import pyproj
from shapely.geometry.polygon import Polygon
from shapely.geometry.point import Point
import fiona
from . import data

STATEPLANES = []

with fiona.open('/stateplane.geojson',
                vfs='zip://' + os.path.join(os.path.dirname(__file__), 'data/stateplane.zip')) as src:
    for f in src:
        f['geometry'] = Polygon(f['geometry'])
        STATEPLANES.append(f)


def get_stateplane(lon, lat, fmt=None):
    '''Return stateplane for given X, Y coordinates
    Defaults to returning EPSG code. Possible fmt parameters: fips, abbr (e.g. 'NY_LI')
    '''
    target = Point(lon, lat)

    for stateplane in STATEPLANES:
        if stateplane['geometry'].contains(target):
            result = stateplane
            break
    try:
        if fmt == 'fips':
            return result['properties']['FIPSZONE83']
        if fmt == 'short':
            return result['properties']['ZONENAME83']
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
            epsg = get_stateplane(x, y)

        if not epsg:
            raise ValueError('Need a ')

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

