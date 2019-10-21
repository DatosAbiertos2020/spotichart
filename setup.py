#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from setuptools import setup

__version__ = ''
with open('spotichart/__about__.py', 'r') as fd:
    reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
    for line in fd:
        m = reg.match(line)
        if m:
            __version__ = m.group(1)
            break


def _requirements():
    with open('requirements.txt', 'r') as fd:
        return [name.strip() for name in fd.readlines()]


with open('README.md', 'r') as fd:
    long_description = fd.read()

setup(
    name="spotichart",
    version=__version__,
    author="Manolomon",
    author_email="contacto@manolomon.com",
    maintainer="Manolomon",
    maintainer_email="contacto@manolomon.com",
    url="https://github.com/Manolomon/spotichart",
    description="Collector Module for Spotify National Trending Analysis",
    long_description=long_description,
    license="License :: OSI Approved :: MIT License",
    packages=[
        "spotichart", "spotichart.spotipy", "spotichart.lyrics", "spotichart.language"
    ],
    install_requires=_requirements(),
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Multimedia :: Sound/Audio :: Analysis"
    ]
)
