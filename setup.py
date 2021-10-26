"""Package manifest for this template repo."""

from setuptools import find_packages, setup

__version__ = "0.1.0"

setup(
    name="src",
    packages=find_packages(),
    version=__version__,
    description="HTM and its applications",
    author="aicoe-aiops",
    license="MIT",
)
