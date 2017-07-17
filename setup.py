# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_django_debug_toolbar import __version__

setup(
    name='aldryn-django-debug-toolbar',
    version=__version__,
    description=open('README.rst').read(),
    author='Joseph Melettukunnel',
    author_email='joseph.melettukunnel@divio.ch',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=["django-debug-toolbar==1.8"],
    include_package_data=True,
    zip_safe=False,
)
