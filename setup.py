#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import os
from codecs import open

with open("README.rst", "r") as f:
    readme = f.read()


def get_packages(package):
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]
