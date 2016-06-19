# from distutils.core import setup
# from Cython.Build import cythonize
# from distutils.extension import Extension
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = 'trnslate app',
    ext_modules = cythonize("ctrans.pyx"),
    # ext_modules = [Extension("ctrans", ["ctrans.pyx"])]
)
