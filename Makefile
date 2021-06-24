.PHONY: update quality tests clean

update:
	pip install -r requirements/dev.txt

quality:
	black --check --diff metaset tests
	flake8 setup.py metaset tests

test:
	pytest --doctest-glob=README.rst --doctest-modules

clean:
	-rm -rf ".cache"
	-rm -rf ".tox"
	-rm -rf "metaset.egg-info"
	-rm -rf "__pycache__"
