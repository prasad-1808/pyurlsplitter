from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.4'
DESCRIPTION = 'A URL splitter tool'
LONG_DESCRIPTION = """
                    Overview\n
In the ever-evolving landscape of web applications and digital platforms, managing and analyzing URLs efficiently is a crucial aspect of cybersecurity, web development, and data analytics. PYURLSPLITTER, a Python tool meticulously crafted for this purpose, empowers users to dissect and manipulate lists of URLs with ease. Whether you're a cybersecurity professional seeking to analyze potential threats, a web developer dealing with URL routing complexities, or a data analyst extracting valuable insights from URLs, PYURLSPLITTER is your go-to solution.\n

Key Features\n
1. URL Splitting Magic\n
PYURLSPLITTER excels at breaking down a list of URLs provided in a text file into their constituent parts. The tool dissects each URL into segments, such as protocol, domain, path, query parameters, and fragments. This granular breakdown serves as the foundation for subsequent analyses and manipulations.\n
\n
2. Comprehensive URL Combinations\n
Not stopping at mere dissection, PYURLSPLITTER takes URL manipulation to the next level by generating various combinations of the dissected URL components. This functionality is particularly useful for scenarios where you need to explore different permutations of URLs, such as testing web application vulnerabilities or optimizing URL structures for SEO purposes.\n
\n
3. Output Refinement\n
The generated URL combinations are presented in a meticulously organized output.txt file. This file not only consolidates the diverse URL combinations but also eliminates any duplicates, providing users with a clean and streamlined dataset for further analysis or implementation.\n
                """

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
    projects_url={
        'Homepage':'https://github.com/prasad-1808/pyurlsplitter.git',
        'Issues':'https://github.com/prasad-1808/pyurlsplitter/blob/master/README.md',
    },
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ]
)
