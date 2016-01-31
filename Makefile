README.rst: README.md
	pandoc $< -o $@ || touch $@
	python setup.py check --restructuredtext --strict

.PHONY: install test
install: README.rst stateplane/data/stateplane.zip
	python setup.py --quiet install

stateplane/data/stateplane.zip: stateplane/data/stateplane.geojson
	rm -f $@
	zip -j $@ $<

.PHONY: deploy
deploy: README.rst | clean
	python3 setup.py sdist bdist_wheel
	rm -r build
	python setup.py sdist
	twine upload dist/*
	git push
	git push --tags

test:
	python setup.py test
	stateplane -73 46
	stateplane -74 42 -o proj4
	stateplane -78 36 -o epsg
	stateplane -77 46 -o short

clean:; rm -r build dist