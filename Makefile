README.rst: README.md
	pandoc $< -o $@ || touch $@

.PHONY: install test
install: README.rst stateplane/data/stateplane.zip
	python setup.py --quiet install

stateplane/data/stateplane.zip: stateplane/data/stateplane.geojson
	rm -f $@
	zip -j $@ $<

.PHONY: deploy
deploy: README.rst
	rm -r dist
	python3 setup.py sdist bdist_wheel
	python setup.py sdist
	twine upload dist/*
	git push
	git push --tags

test:
	python setup.py test
	$$(which python | xargs dirname)/stateplane -73 46
	$$(which python | xargs dirname)/stateplane -74 42 -o proj4
	$$(which python | xargs dirname)/stateplane -78 36 -o epsg
	$$(which python | xargs dirname)/stateplane -77 46 -o short

