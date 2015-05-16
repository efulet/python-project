"""
@created_at 2015-05-11
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import sys

import project


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name='Project',
    version='1.0.0',
    author='Exequiel Fuentes Lettura',
    author_email='efulet@gmail.com',
    url='http://github.com/efulet/project/',
    license='LICENSE.md',
    description='A basic structure of your skeleton directory',
    packages=['project'],
    include_package_data=True,
    platforms='any',
    test_suite='project.test',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    install_requires=['cov-core==1.15.0',
                      'coverage==3.7.1',
                      'docutils==0.12',
                      'pytest==2.7.0',
                      'pytest-cov==1.8.1',
                      'Sphinx==1.3.1',
                      'SQLAlchemy==1.0.4'],
    extras_require={
        'testing': ['pytest'],
    }
)
