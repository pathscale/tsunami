from .test cimport test as rjwtest
from libcpp cimport bool
from ..utils.utils import _chars, _text
import cython

def test(str json="{}"):
    cdef:
        bytes bstr = _chars(json)
        char* jsonChar = bstr
        int output = rjwtest.test(jsonChar)
    print(output)

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.final
cdef class Document:
    """
    Document JSON class

    manipulate JSON file in python and cython
    """
    cdef:
        rjwtest.Doc doc

    def __cinit__(self):
        self.doc = rjwtest.Doc()

    def __cinit__(self):
        self.doc = rjwtest.Doc()

    """Parser of json string to document"""
    cdef:
        void _Parser(self, char*json) nogil:
            self.doc.Parse(json)
        void Parse(self, char*json) nogil:
            self._Parser(json)
    def Parse(self, str json):
        """
        Parse string json to document json

        Args:
            json (str): python string json
        """
        self._Parser(_chars(json))

    """error handling"""
    cdef:
        bool _HasError(self) nogil:
            return self.doc.HasError()
        bool HasError(self) nogil:
            return self._HasError()
    def HasError(self):
        """
        HasError check json contain any errors

        Returns:
            bool: if contain any error return False, else True
        """
        return self._HasError()

    cdef:
        char*_GetError(self) nogil:
            return self.doc.GetError()
        char*GetError(self) nogil:
            return self._GetError()
    cpdef GetErrorBytes(self):
        """
        GetError return error message

        Returns:
            bytes: error message
        """
        return self._GetError()
    def GetError(self):
        """
        GetError return error message

        Returns:
            str: error message
        """
        toParse = self.GetErrorBytes()
        return _text(toParse)

    def __dealloc__(self):
        pass
        #del self.doc
