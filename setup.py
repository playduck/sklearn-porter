# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

from os.path import abspath
from os.path import dirname
from os.path import exists
from os.path import join
from json import load

setup(
    name="sklearn-porter",
    description="Transpile trained scikit-learn models to C, Java, JavaScript and others.",
    long_description="file://../readme.md",
    long_description_content_type='text/markdown',
    keywords=["sklearn", "scikit-learn"],
    url="https://github.com/nok/sklearn-porter",
    author="Darius Morawiec",
    author_email="nok@users.noreply.github.com",
    install_requires=[
        "six",
        "scikit-learn>=0.14.1"
    ],
    packages=find_packages(exclude=["tests.*", "tests"]),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'porter = sklearn_porter.cli.__main__:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    version="0.7.4",
    license="MIT"
)
