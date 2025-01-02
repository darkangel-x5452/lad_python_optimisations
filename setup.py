# from distutils.core import setup

from Cython.Build import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize("data_methods/methods/count_past_matches.pyx")
)
