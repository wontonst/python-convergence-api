from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='convergence-api',
      version='0.2',
      description='A simple, easy to use wrapper for Elavon\'s Converge API via key value pairs instead of XML',
      url='http://github.com/wontonst/python-convergence-api',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      author='Roy Zheng',
      license='MIT',
      install_requires=['requests'],
      zip_safe=False)
