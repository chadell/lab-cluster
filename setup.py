#!/usr/bin/env python
# pylint: disable=attribute-defined-outside-init
import sys
import os
from pip.req import parse_requirements
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


def get_version():
    version = os.environ.get('VERSION')
    if version is None:
        version = '0.0.1'
    return version


class PyTest(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['--cov=mesos_api', '--cov-report',
                            'term-missing', '-v', '-s', '--flake8', '--pylint']

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='mesos_api',
    version=get_version(),
    description='Mesos API',
    author='Christian Adell',
    author_email='chadell@gmail.com',
    packages=find_packages(),
    entry_points={'console_scripts': [
        'mesos-api = mesos_api.api:main'
    ]},
    install_requires=[str(req.req) for req in parse_requirements('mesos_api/requirements.txt', session=False)],
    tests_require=[str(req.req) for req in parse_requirements('mesos_api/test_requirements.txt', session=False)],
    cmdclass={'test': PyTest},
    test_suite='tests',
)
