from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "core.wrappers.rapidjson_wrapper.rapidjson",
        sources=[
            "core/wrappers/rapidjson_wrapper/rjson_wrapper.pyx",
        ],
        include_dirs=["core/wrappers/rapidjson_wrapper/test"],
        language="c++",
    ),
    Extension(
        "core.wrappers.utils.utils",
        sources=[
            "core/wrappers/utils/utils.pyx",
        ],
        include_dirs=["core/wrappers/utils"],
        language="c++",
    ),
]
ext_tests = [
    Extension(
        "core.cy_tests.tests",
        sources=[
            "core/cy_tests/rjson_wrapper_test.pyx",
        ],
        include_dirs=[
            "core/wrappers/rapidjson_wrapper/test",
            "core/wrappers/utils"
        ],
        language="c++",
    ),
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
