#!/usr/bin/env python

from setuptools import setup, find_packages
import io

setup(
    name='tomago-sdk-py',
    version='1.5.1',
    description="Python SDKs for Blockchain."
    long_description=io.open('README.md', encoding='utf-8').read(),
    url='https://github.com/arxanchain/tomago-sdk-py/',
    download_url='https://github.com/arxanchain/tomago-sdk-py/',
    packages=find_packages(),
    platforms='any',
    install_requires=[
        "mock==2.0.0",
        "requests==2.18.4",
        "six==1.11.0",
        "urllib3==1.22",
        "py-common==v1.5.1"
        ],
    dependency_links=[
        "git+git://github.com/arxanchain/py-common.git@master#egg=py-common-v1.5.1"
    ],
    include_package_data=True,
    zip_safe=False,
)
