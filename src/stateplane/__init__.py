# This file is part of stateplane.
# https://github.com/fitnr/stateplane

# Licensed under the GPLv3 license:
# http://http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>
"""Find the state plane projection for a point or locale"""
from . import stateplane

__version__ = "0.5.0"

_sp = stateplane.Stateplane()

from_latlon = _sp.from_latlon
from_lonlat = _sp.from_lonlat
to_latlon = _sp.to_latlon
to_lonlat = _sp.to_lonlat
identify = _sp.identify
