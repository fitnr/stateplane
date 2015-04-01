.PHONY: setup
setup: readme.rst stateplane/data/stateplane.zip
	python setup.py install

readme.rst: readme.md
	pandoc $< -o $@ || touch readme.rst

stateplane/data/stateplane.zip: stateplane/data/stateplane.geojson
	rm -f $@
	zip -j $@ $<

stateplane/data/stateplane.geojson: stateplane/data/stateplane.shp
	ogr2ogr -f GeoJSON $@ $<
