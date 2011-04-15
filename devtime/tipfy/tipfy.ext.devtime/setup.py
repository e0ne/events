# -*- coding: utf-8 -*-
"""
    tipfy.ext.devtime
    ~~~~~~~~~~~~~~~~~

    Sample extension for DevTime

    :copyright: 2011 Ivan Kolodyazhny.
    :license: Apache, see LICENSE.txt for more details.
"""
from setuptools import setup

setup(
    name = 'tipfy.ext.devtime',
    version = '0.1',
    license = 'Apache',
    url = 'http://blog.e0ne.info',
    description = 'Sample extension for DevTime',
    long_description = __doc__,
    author = 'Ivan Kolodyazhny',
    author_email = 'e0ne@e0ne.info',
    zip_safe = False,
    platforms = 'any',
    packages = [
        'tipfy',
        'tipfy.ext',
    ],
    namespace_packages = [
        'tipfy',
        'tipfy.ext',
    ],
    include_package_data = True,
    install_requires = [
        'tipfy',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)