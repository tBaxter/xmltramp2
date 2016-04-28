# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='xmltramp2',
    version='3.1.1',
    author=u'Tim Baxter',
    author_email='mail.baxter@gmail.com',
    description='A modern refactoring of the venerable xmltramp application',
    long_description=open('README.md').read(),
    url='https://github.com/tBaxter/xmltramp2',
    license='GPL',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
          'six',
    ],
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
