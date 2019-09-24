#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

__version__ = ''
with open('topsipy/__about__.py', 'r') as fd:
    reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
    for line in fd:
        m = reg.match(line)
        if m:
            __version__ = m.group(1)
            break


def _requirements():
    with open('requirements.txt', 'r') as fd:
        return [name.strip() for name in fd.readlines()]


def _requirements_test():
    with open('requirements-test.txt', 'r') as fd:
        return [name.strip() for name in fd.readlines()]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


with open('README.md', 'r') as fd:
    long_description = fd.read()

setup(
    name="topsipy",
    version=__version__,
    author="Manolomon",
    author_email="contacto@manolomon.com",
    maintainer="Manolomon",
    maintainer_email="contacto@manolomon.com",
    url="https://github.com/Manolomon/topsipy",
    description="Spotify top 50 and audio feature scrapper, with lyrics and annotations from Genius",
    long_description=long_description,
    license='MIT',
    packages=[
        "topsipy", "topsipy.spotipy", "topsipy.pyrics"
    ],
    install_requires=_requirements(),
    tests_require=_requirements_test(),
    cmdclass={'test': PyTest},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development"
    ]
)