.PHONY: update quality tests clean

update:
	pip install -r requirements.txt

quality:
	flake8 setup.py metaset

test:
	nosetests metaset

test_docstring:
	nosetests --with-doctest metaset/__init__.py

clean:
	-rm -rf ".cache"
	-rm -rf ".tox"
	-rm -rf "metaset.egg-info"
	-rm -rf "__pycache__"
