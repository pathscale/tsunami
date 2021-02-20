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
    cdef rjwtest.Doc doc

    def __init__(self, json):
        self.doc = rjwtest.Doc(_chars(json))

    cpdef bool HasError(self):
        return self.doc.HasError()

    cdef char* GetError(self):
        return self.doc.GetError()

    def GetError(self):
        return _text(self.doc.GetError())

    def __dealloc__(self):
        pass
        #del self.doc
