.PHONY: install test
install: readme.rst stateplane/data/stateplane.zip
	python setup.py --quiet install

stateplane/data/stateplane.zip: stateplane/data/stateplane.geojson
	rm -f $@
	zip -j $@ $<

readme.rst: readme.md
	pandoc $< -o $@ || touch readme.rst

test:
	python setup.py test
	stateplane -73 46
	stateplane -74 42 -o proj4
	stateplane -78 36 -o epsg
	stateplane -77 46 -o short
