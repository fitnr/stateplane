#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of stateplane.
# https://github.com/fitnr/stateplane

# Licensed under the GPLv3 license:
# http://http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015, Neil Freeman <contact@fakeisthenewreal.org>

from . import stateplane

__version__ = '0.4.1'

identify = stateplane.identify

_sp = stateplane.Stateplane()

from_latlon = _sp.from_latlon
from_lonlat = _sp.from_lonlat
to_latlon = _sp.to_latlon
to_lonlat = _sp.to_lonlat
