#!/usr/bin/env python2.7
# coding:utf-8
#
#
#

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(cmdclass={'build_ext': build_ext},
     ext_modules=[Extension("generator", ["cython-generator.pyx"])]
    )

if __name__ == '__main__':
    pass
