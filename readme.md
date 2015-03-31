pystateplane
------------

Get the local state plane projection for geographica coordinates, and automatically convert between coordinates and the local state plane projection.

Find the local state plane system:
````python
import stateplane

# Returns the EPSG value for this (lon, lat)
stateplane.identify(-73.2, 43.2)
# 32145

# Return a short name for the projection
stateplane.identify(-88.2, 41.2, 'short')
# 'IL_E'

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

