#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://flask-restless-swagger.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='flask-restless-swagger',
    version='0.2.1',
    description='Magically create swagger documentation as you magically create your RESTful API',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Michael Messmore',
    author_email='mike@messmore.org',
    url='https://github.com/mmessmore/flask-restless-swagger',
    packages=[
        'flask_restless_swagger',
    ],
    package_dir={'flask_restless_swagger': 'flask_restless_swagger'},
    include_package_data=True,
    install_requires=[
        'Flask>=0.10.0',
        'Flask-Restless>=0.17.0'
    ],
    license='BSD',
    zip_safe=False,
    keywords='flask-restless-swagger',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
