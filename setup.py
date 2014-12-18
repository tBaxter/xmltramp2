# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(
    name='xmltramp2',
    version='3.0.0',
    author=u'Tim Baxter',
    author_email='mail.baxter@gmail.com',
    packages=find_packages(),
    url='https://github.com/tBaxter/xmltramp2',
    license='GPL',
    description='A modern refactoring of the venerable xmltramp application',
    long_description=open('README.md').read(),
    include_package_data=True,
    zip_safe=False,
)
