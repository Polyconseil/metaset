# Copyright (c) Polyconseil SAS. All rights reserved.
from setuptools import find_packages, setup


def read(filename):
    with open(filename) as fp:
        return fp.read()


setup(
    name='metaset',
    version='1.0.0',
    author='Polyconseil dev team',
    author_email='autolib-dev@polyconseil.fr',
    description='A container for dicts of sets - alternative to dictset',
    license='BSD',
    keywords=['metaset', 'dictset', 'set', 'container'],
    url='https://github.com/Polyconseil/metaset',
    download_url='http://pypi.python.org/pypi/metaset/',
    bugtrack_url='https://github.com/Polyconseil/metaset/issues',
    packages=find_packages(),
    long_description=read('README.md'),
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Natural Language :: English',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    include_package_data=True,
)
