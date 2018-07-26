import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='envutils',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/mfilippo/envutils',
    license='MIT',
    author='Matteo Filipponi',
    author_email='matteofilipponi@hotmail.com',
    description='A python library to read and parse environment variables.',
    long_description=README,
    long_description_content_type='text/markdown',
)
