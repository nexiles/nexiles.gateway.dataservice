# -*- coding: utf-8 -*-
"""
This module contains the tool of sample
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1dev'

long_description = (read('README.rst'))

setup(name='nexiles.gateway.dataservice',
      version=version,
      description="nexiles.gateway.dataservice",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='',
      author='Stefan Elethofer',
      author_email='stefan.eletzhofer@nexiles.com',
      url='https://github.com/nexiles/nexiles.tools',
      license='proprietary',
      packages=find_packages('.', exclude=['ez_setup']),
      package_dir={'': '.'},
      namespace_packages=['nexiles', 'nexiles.gateway.dataservice'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'simplejson==2.2.1',
                        'flask==0.8',
                        # -*- Extra requirements: -*-
                        ],
      )
