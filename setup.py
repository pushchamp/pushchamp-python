"""
    A setuptools based setup module.
"""

import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


def get_version():
    """
        return current version of this SDK.
    """
    init = open(os.path.join(ROOT, 'pushchamp', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='pushchamp',
    version=get_version(),
    description='The PushChamp SDK for Python',
    long_description=open('README.rst').read(),
    author='Pushchamp Technologies',
    author_email='info@pushchamp.com',
    url='https://github.com/pushchamp/pushchamp-python',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    package_data={},
    include_package_data=True,
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
