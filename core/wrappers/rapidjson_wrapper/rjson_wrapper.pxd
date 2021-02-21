from .test cimport test as rjwtest
from libcpp cimport bool

cdef char* _chars(str pystring):
    cdef:
        bytes bstr = pystring.encode('utf-8')
        char* s = bstr
    return s

cdef str _text(char* charstr):
    return charstr.decode('utf-8')



def test(str json="{}"):
    cdef:
        char* jsonChar = _chars(json)
        int output = rjwtest.test(jsonChar)
    print(output)




cdef class Document():
    cdef readonly rjwtest.Doc doc

    cdef readonly void _Parser(self, char* json) nogil:
        self.doc = rjwtest.Doc(json)

    cdef void Parse(self, char* json) nogil:
        self._Parser(json)

    def Parse(self, str json):
        self._Parser(_chars(json))

    cpdef bool HasError(self) nogil:
        return self.doc.HasError()

    cdef readonly char* _GetError(self) nogil:
        return self.doc.GetError()

    cdef char* GetError(self) nogil:
        return self._GetError()

    def GetError(self):
        return self._GetError()

    def __dealloc__(self):
        pass
        #del self.doc
