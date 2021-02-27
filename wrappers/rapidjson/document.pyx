cimport cdocument as cdoc

cdef str ctopy(text):
    return text.decode('UTF-8')

cdef const char* pytoc(text):
    cdef const char* _text
    btext = text.encode('UTF-8')
    _text = btext
    return _text

cdef class Document:
    cdef cdoc.Doc doc
    def __init__(self, json):
        self.doc = cdoc.Doc(pytoc(json))

    cpdef set_int(self, key, value):
        if not key is None and not value is None:
            self.doc.set_int(pytoc(key), value)
        else:
            raise TypeError

    cpdef set_string(self, key, value):
        if not key is None and not value is None:
            key = pytoc(key)
            value = pytoc(value)
            self.doc.set_string(key, value)
        else:
            raise TypeError

    # cpdef add_int(self, key, value):
    #     if not key is None and not value is None:
    #         self.doc.add_int(pytoc(key), value)
    #     else:
    #         raise TypeError

    cpdef get_int(self, val):
        return self.doc.get_int(pytoc(val))

    cpdef get_string(self, val):
        return ctopy(self.doc.get_string(pytoc(val)))

    cpdef get_json(self):
        return ctopy(self.doc.get_json())
