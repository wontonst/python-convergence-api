from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='convergence-api',
      version='0.1',
      description='A simple, easy to use wrapper for Elavon\'s Converge API via key value pairs instead of XML',
      url='http://github.com/wontonst/python-convergence-api',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Roy Zheng',
      license='MIT',
      install_requires=['requests'],
      zip_safe=False)
