from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "core.wrappers.rapidjson_wrapper.rapidjson",
        sources=[
            "core/wrappers/rapidjson_wrapper/rjson_wrapper.pyx",
            # "core/third-party/rapidjson_wrapper/include/rapidjson_wrapper/schema.h",
        ],
        include_dirs=["core/wrappers/rapidjson_wrapper/test"],
        language="c++",
    )
]
setup(
    ext_modules=cythonize(ext_modules),
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
