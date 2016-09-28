.PHONY: update quality tests clean

update:
	pip install -r requirements.txt

quality:
	flake8 setup.py __init__.py

test:
	nosetests tests.py

clean:
	-rm -rf ".cache"
	-rm -rf ".tox"
	-rm -rf "metaset.egg-info"
	-rm -rf "__pycache__"
