from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'A basic URL splitter tool'
LONG_DESCRIPTION = 'A basic tool for generating different combinations of url with subdirectories for the given target urls'

# Setting up
setup(
    name="pyurlsplitter",
    version=VERSION,
    scripts=['pyurlsplitter/urlsplitter.py'],
    author="Prasad D",
    author_email="<prasadd.1808@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
     entry_points={
        'console_scripts': [
            'pyurlsplitter = pyurlsplitter.urlsplitter:main',
        ],
    },
    install_requires=[],
    keywords=['python', 'url', 'url-splitter', 'endpoint splitter', 'subdirectory', 'recon-tool'],
    classifiers=[
    ]
)