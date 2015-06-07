# -*- coding: utf-8 -*-

from __future__ import division

__author__ = 'christoph.statz <at> tu-dresden.de'

from setuptools import find_packages, setup

setup(name='mauivs',
      version='0.0.1',
      description='This module implements vizschema 3.0 output for maui.',
      author='Christoph Statz',
      author_email='christoph.statz@tu-dresden.de',
      url='http://www.cstatz.de',
      packages=find_packages(),
      install_requires=['numpy>=1.8.0', 'h5py>=2.3.0'],
      )
