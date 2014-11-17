#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import djangotoolbox, django_mongodb_engine

package_name = 'django-nosql'

def runtests():
    import os
    import sys
    
    import django
    from django.core.management import call_command
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_nonrel_test_project.settings'
    if django.VERSION[0] == 1 and django.VERSION[1] >= 5:
        setup()
    call_command('test', 'djangotoolbox')

    sys.exit()

setup(name='django-nonrel',
    description="Django Nonrel Package",
    author='unknown',
    author_email='hung@greyside.co',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords='django nosql',
    download_url='https://github.com/Hn23/django-nosql',
    license='GPL',
    packages=[
        'djangotoolbox',
        'django_nonrel_test_project',
        'django_mongodb_engine',
    ],
    include_package_data=True,
    install_requires=[],

 #   tests_require=['django-admin-smoke-tests>=0.1.8',],

    test_suite='setup.runtests',
)
