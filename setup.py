import os
import sys
import platform
import setuptools
import configparser

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()


# config
config = configparser.ConfigParser()
current_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_directory, 'setup.cfg')

config.read(config_file_path)


# meta
AUTHOR = config['tob']['author']
AUTHOR_EMAIL = config['tob']['email']
DESCRIPTION = config['tob']['description']
NAME = config['tob']['name']
VERSION = config['tob']['version']
URL = config['tob']['url']


# requirements
REQUIREMENTS = []
DEPENDENCIES = []

with open('requirements.txt') as requirements:
    for requirement in requirements.readlines():
        if requirement.startswith('git+git://'):
            DEPENDENCIES.append(requirement)
        else:
            REQUIREMENTS.append(requirement)


# setup
setuptools.setup(
    name="tob",
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
