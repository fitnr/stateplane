# This file is part of stateplane.
# https://github.com/fitnr/stateplane

# Licensed under the GPLv3 license:
# http://http://opensource.org/licenses/GPL-3.0
# Copyright (c) 2015-22, Neil Freeman <contact@fakeisthenewreal.org>
SHELL := /bin/bash

.PHONY: install test release

install:
	python -m pip install .

cover: | test
	coverage report --fail-under 80

test:
	coverage run -m unittest
	stateplane -73 46
	stateplane -78 36 -o epsg
	stateplane -77 46 -o short

public: | build
	twine upload dist/*

build: | clean
	python3 -m build

clean:; rm -fr build dist
