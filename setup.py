# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(
    name='xmltramp2',
    version='3.0.3',
    author=u'Tim Baxter',
    author_email='mail.baxter@gmail.com',
    packages=find_packages(),
    url='https://github.com/tBaxter/xmltramp2',
    license='GPL',
    description='A modern refactoring of the venerable xmltramp application',
    long_description=open('README.md').read(),
    include_package_data=True,
    install_requires=[
          'six',
    ],
    zip_safe=False,
    classifiers=(
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Text Processing :: Markup :: XML",
    ),
)
