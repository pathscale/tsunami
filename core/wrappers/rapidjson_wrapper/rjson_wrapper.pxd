from .test cimport test as rjwtest
from libcpp cimport bool
import cython


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.final
cdef class Document:
    cdef:
        rjwtest.Doc doc
        void _Parser(self, char*json) nogil
        void Parse(self, char*json) nogil
        bool _HasError(self) nogil
        bool HasError(self) nogil
        char*_GetError(self) nogil
        char*GetError(self) nogil
