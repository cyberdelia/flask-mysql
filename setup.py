# -*- coding: UTF-8 -*-
from setuptools import setup


setup(
    name='Flask-MySQL',
    version='1.3',
    url='https://github.com/cyberdelia/flask-mysql/',
    license='BSD',
    author='Timothee Peignier',
    author_email='timothee.peignier@tryphon.org',
    description='Flask simple mysql client',
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'MySQL-python'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
