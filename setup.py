# -*- coding: utf-8 -*-
from setuptools import setup
__version__ = ''


def _requirements():
    with open('requirements.txt', 'r') as fd:
        return [name.strip() for name in fd.readlines()]


def _long_description():
    with open('README.rst', 'r') as fd:
        long_description = fd.read()
    return long_description


setup(
    name="oneplatform-sdk",
    version=__version__,
    author="INET-SDI",
    author_email="inet-sdi@inet.co.th",
    maintainer="INET-SDI",
    maintainer_email="inet-sdi@inet.co.th",
    url="https://github.com/inetspa/oneplatform-sdk-python",
    description="OnePlatform API SDK for Python",
    long_description=_long_description(),
    license='GNU GPL 3.0',
    packages=[
        "oneid"
    ],
    install_requires=_requirements(),
    classifiers=[
        "License :: OSI Approved :: GNU GPL v.3.0 Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development"
    ]
)
