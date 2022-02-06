.PHONY: install test
install:
	python setup.py install

.PHONY: deploy
deploy: README.rst | clean
	python3 setup.py sdist bdist_wheel
	rm -fr build
	python setup.py sdist
	twine upload dist/*
	git push
	git push --tags

test:
	python -m unittest
	stateplane -73 46
	stateplane -78 36 -o epsg
	stateplane -77 46 -o short

clean:; rm -fr build dist