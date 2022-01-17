import os

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(os.path.join(os.path.dirname(__file__), "requirements.txt")) as f:
    INSTALL_REQUIRES = f.read().splitlines()

setup(
    name="betfairmarketvolumesclient",
    version="0.0.4",
    author="Oliver Varney",
    author_email="oliverashleyvarney@gmail.com",
    description="Simple file downloader for the betfair daily sp files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="core packages",
    url="https://github.com/varneyo/betfairmarketvolumesclient",
    package_dir={"betfairmarketvolumesclient": "betfairmarketvolumesclient"},
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(exclude=["examples"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    test_suite="tests",
)
