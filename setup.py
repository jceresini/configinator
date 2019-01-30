"""Packaging settings."""
from setuptools import setup
setup(
    name='configinator',
    description='A simple config loading library.',
    author="Joe Ceresini",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=['configinator'],
    install_requires=[
        'future'
    ],
    license="Apache 2.0"
)
