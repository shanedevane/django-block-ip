#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(
    name='django-block-ip',
    version='0.3.0',
    url='http://github.com/shanedevane/django-block-ip',
    license='BSD',
    description='Simple IP and IP-range blocking for Django',
    long_description=open('README.md', 'r').read(),
    author='Philip Neustrom, Shane Devane',
    author_email='philipn@gmail.com, shanedevane@gmail.com',
    packages=get_packages('block_ip'),
    package_data=get_package_data('.'),
    install_requires=[
        'ipcalc',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
