from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    # Extension("wrappers.rapidjson.rapidjson",
    #           sources=[
    #               "wrappers/rapidjson/rapidjson.pyx"
    #           ],
    #           include_dirs=["wrappers/rapidjson"],
    #           language="c++",
    #           ),
    Extension(
        "wrappers.rapidjson.document",
        sources=["wrappers/rapidjson/document.pyx"],
        include_dirs=["wrappers/rapidjson"],
        language="c++",
    ),
    Extension(
        "tests",
        sources=["tests.pyx"],
        include_dirs=["wrappers/rapidjson"],
        language="c++",
    ),
]
setup(
    ext_modules=cythonize(ext_modules),
    zip_safe=False,
    name="hw",
    version="0.1",
    packages=["cython"],
    url="lols",
    license="MIT",
    author="kacpe",
    author_email="me@xd",
    description="test",
)
