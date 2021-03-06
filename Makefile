.PHONY: update quality tests clean

update:
	pip install -r requirements/dev.txt

quality:
	black -q --diff metaset tests
	flake8 setup.py metaset tests

test:
	nosetests tests

test_docstring:
	nosetests --with-doctest metaset
	python -m doctest README.rst

clean:
	-rm -rf ".cache"
	-rm -rf ".tox"
	-rm -rf "metaset.egg-info"
	-rm -rf "__pycache__"
