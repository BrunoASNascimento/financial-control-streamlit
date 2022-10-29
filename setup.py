"""Python Setup"""
from setuptools import setup, find_packages

VERSION = '0.0.1'

# README.MD to long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# requirements.txt to install_requires
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="financial-control-streamlit",
    version=VERSION,
    description="",
    long_description=long_description,
    author="AUTHOR",
    author_email="bruno-asn@hotmail.com",
    license='MIT',
    install_requires=required,
    extras_require={},
    classifiers=[],
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires=">=3.10",
)
