# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='totem',
    version="1",
    packages=find_packages(),
    author="megadose",
    install_requires=["argparse","fake_useragent"],
    description="",
    long_description="",
    include_package_data=True,
    url='http://github.com/megadose/totem',
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
