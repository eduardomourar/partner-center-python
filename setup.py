#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import setup, find_packages

NAME = 'partnercenterservices'

REQUIRES = ['msrestazure>=0.4.7']

with io.open('README.md', 'r') as fh:
    long_description = fh.read()

metadata = {}
version_filename = os.path.join(os.path.dirname(__file__), 'microsoft', 'store', 'partnercenterservices', 'version.py')
exec(os.open(version_filename).read(), None, metadata)

setup(
    name=NAME,
    version=metadata['VERSION'],
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
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
