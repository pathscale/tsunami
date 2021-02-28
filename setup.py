from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
]
ext_tests = [
]
setup(
    ext_modules=cythonize(list(ext_modules+ext_tests)),
    zip_safe=False,
    name="tsunami",
    version="0.1",
    packages=["cython"],
    url="lols",
    license="MIT",
    author="kacpe",
    author_email="me@xd",
    description="test",
)
