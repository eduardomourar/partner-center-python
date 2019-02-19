#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io

from setuptools import setup, find_packages

NAME = 'partnercenterservices'
VERSION = '0.1.2'

REQUIRES = ['msrestazure>=0.4.7']

with io.open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description='Python SDK for Microsoft Partner Center Services API',
    author='Eduardo Rodrigues',
    author_email='',
    url='https://github.com/eduardomourar/partner-center-python',
    keywords=['api', 'microsoft', 'partnercenter'],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT'
)
