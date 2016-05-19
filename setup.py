# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_django_debug_toolbar import __version__

setup(
    name='aldryn-django-debug-toolbar',
    version=__version__,
    description=open('README.rst').read(),
    author='Rob Hudson',
    author_email='rob@cogit8.org',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[
        'Django>=1.7',
        'sqlparse',
        'django-debug-toolbar==1.4',
        'aldryn-addons',
    ],
    include_package_data=True,
    zip_safe=False,
    license='BSD',
)
