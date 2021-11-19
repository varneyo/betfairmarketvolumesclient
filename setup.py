import os

from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with open(os.path.join(os.path.dirname(__file__), "requirements.txt")) as f:
    INSTALL_REQUIRES = f.read().splitlines()

setup(
    name="betfairmarketvolumesclient",
    version="0.0.1",
    author="Oliver Varney",
    author_email="oliverashleyvarney@gmail.com",
    description=("Simple api to make requests to timeform endpoints"),
    license="MIT",
    keywords="core packages",
    url="https://github.com/varneyo/timeform",
    package_dir={"betfairmarketvolumesclient": "betfairmarketvolumesclient"},
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(
        exclude=["examples"]
    ),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    test_suite="tests",
)
