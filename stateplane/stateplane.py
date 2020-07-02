import os.path
from csv import reader
from json import loads
from osgeo import ogr, osr
import pyproj
from shapely.geometry import shape
from shapely.geometry.point import Point
from . import dicts

GEOJSON = os.path.join(os.path.dirname(__file__), 'data/stateplane.geojson')
CSV = os.path.join(os.path.dirname(__file__), 'data/countyfp.csv')


def _load_boundaries():
    features = []
    src = ogr.Open(GEOJSON, 0)
    layer = src.GetLayer()
    for n in range(layer.GetFeatureCount()):
        f = loads(layer.GetFeature(n).ExportToJson())
        f['geometry'] = shape(f['geometry'])
        features.append(f)

    del src
    return features


def _cofips():
    with open(CSV) as rs:
        r = reader(rs, delimiter=',')
        next(r)
        return {fp: epsg for fp, epsg in r}


STATEPLANES = _load_boundaries()
COFIPS = _cofips()


def _get_co(countyfp, statefp=None):
    if statefp and len(countyfp) == 3:
        countyfp = statefp + countyfp

    if not COFIPS:
        _cofips()

    try:
        return COFIPS[countyfp]
    except KeyError:
        # Guess the countyfp didn't work
        pass


def _id(lon, lat, statefp=None, countyfp=None):
    stateplanes = None
    if countyfp:
        epsgmatch = _get_co(countyfp, statefp)
        if epsgmatch:
            stateplanes = [s for s in STATEPLANES if s['properties']['EPSG'] == epsgmatch]

    elif statefp:
        stateplanes = [s for s in STATEPLANES if s['properties']['STATEFP'] == str(statefp)]

    else:
        stateplanes = STATEPLANES

    if not stateplanes:
        raise ValueError("SPCS not found for statefp={}".format(statefp))

    if len(stateplanes) == 1:
        return stateplanes[0]

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


def identify(lon, lat, fmt=None, statefp=None, countyfp=None):
    '''Return stateplane for given X, Y coordinates
    Defaults to returning EPSG code. Possible fmt parameters: fips, abbr (e.g. 'NY_LI')
    '''
    result = _id(lon, lat, statefp=statefp, countyfp=countyfp)

    try:
        if fmt == 'fips':
            return result['properties']['FIPSZONE83']

        if fmt == 'short':
            return result['properties']['ZONENAME83']

        if fmt == 'proj4':
            sr = osr.SpatialReference()
            sr.ImportFromEPSG(int(result['properties']['EPSG']))
            return sr.ExportToProj4()

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
            epsg = dicts.FIPS_TO_EPSG[fips]
        elif abbr:
            epsg = dicts.SHORT_TO_EPSG[abbr]

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
        lon, lat = self.to_lonlat(easting, northing, epsg, fips, abbr)
        return lat, lon

    def to_lonlat(self, easting, northing, epsg=None, fips=None, abbr=None):
        '''Return (lon, lat) from a state plane (easting, northing) pair.
        Must pass either a fips code, epsg, or abbr to specify the state plane projection to use
        '''
        if not any((epsg, fips, abbr)):
            raise ValueError("to long/lat calculations require a epsg, fips or abbr argument.")
        return self._convert(easting, northing, True, epsg, fips, abbr)
