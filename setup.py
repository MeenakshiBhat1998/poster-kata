"""
Installs Command Line Utilities
"""
import os
from setuptools import setup, find_packages


def readlines(fname):
    """
    Read lines from the given file and strip any non printable characters while returning
    :param fname: File name
    :return: list of lines
    """
    with open(os.path.join(os.path.dirname(__file__), fname), "r") as file:
        return [line.strip() for line in file]


setup(
    name="poster-kata",
    version="1.0.4",
    install_requires=readlines("requirements.txt"),
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        poster-kata=app.command:cli
    """
)
