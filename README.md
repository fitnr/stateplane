# pystateplane

Get the local state plane projection for geographica coordinates, and automatically convert between coordinates and the local state plane projection.

Includes state plane projections for the 50 states, DC, Puerto Rico, American Samoa, Guam and the US Virgin Islands.

Find the local state plane system:
````python
import stateplane

# Returns the EPSG value for this (lon, lat)
stateplane.identify(-73.2, 43.2)
# 32145

# Return a short name for the projection
stateplane.identify(-88.2, 41.2, 'short')
# 'IL_E'

# Speed up the process by specifying a state FIPS code
stateplane.identify(-88.2, 41.2, 'short', statefp='17')
# 'IL_E'

# Speed up the process even more by specifying a county FIPS code
# These two calls are equivalent
stateplane.identify(None, None, 'short', countyfp='36005')
stateplane.identify(None, None, 'short', statefp='36', countyfp='005')
# 'NY_LI'

stateplane.identify(-80.1, 36.2, fmt='short')
# 'NC'

# returns the FIPS code of the projection
stateplane.identify(-80.1, 36.2, fmt='fips')
'3200'
````

Convert to the (easting, northing) of the local state plane:

````python
stateplane.from_lonlat(-80.1, 36.2)
(510673.2830651368, 272340.60789450357)

stateplane.from_lonlat(-75.2, 40.2)
(817080.8169336573, 99364.28495057777)

stateplane.identify(-75.2, 40.2, fmt='short')
'PA_S'
````

## Installing

Assuming you have [pip](https://pip.pypa.io/en/stable/), run:
````bash
pip install stateplane
````

Or, download the repository and run:
````bash
python setup.py install
````

## Functions

#### stateplane.identify(lon, lat, fmt=None, statefp=None)

#### from_latlon(lat, lon, epsg=None, fips=None, abbr=None, statefp=None, countyfp=None)
#### from_lonlat(lon, lat, epsg=None, fips=None, abbr=None, statefp=None, countyfp=None)

For these functions, `epsg`, `fips` or `abbr` can be used to specify a projection.
The `statefp` parameter can be used to specify a two-digit state (or territory) FIPS code, while results in more efficient checking.
Use `countyfp` to specify a five-digit county FIPS code. Or, in combination with `statefp`, use the three-digit county stem.

### to_latlon(easting, northing, epsg=None, fips=None, abbr=None)
### to_lonlat(easting, northing, epsg=None, fips=None, abbr=None)

For these functions, as least one of `epsg`, `fips` and `abbr` must be provided.

## Caveats

This module is really just a convenience wrapper for the excellent `pyproj` library. Big speed gains could be achieved by doing the conversions natively. Pull requests are gladly accepted.
