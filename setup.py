#!/usr/bin/env python
"""Setup."""
import pathlib
import setuptools
import sys


def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    with pathlib.Path(filename).open() as fp:
        lines = (l.split('#')[0].strip() for l in fp)
        return [line for line in lines if line and not line.startswith('--')]


setuptools.setup(
    name='figures',
    version=pathlib.Path('VERSION').read_text().strip(),
    description='Historical figures API',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    author='Iván Calle Gil',
    python_requires='>=3.8',
    packages=setuptools.find_packages(exclude='tests'),
    setup_requires=['pytest-runner'] if 'pytest' in sys.argv else [],
    install_requires=parse_requirements('requirements/install.txt'),
    tests_require=parse_requirements('requirements/test.txt'),
    include_package_data=True,
    zip_safe=True)
