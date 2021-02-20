cimport document

cdef str ctopy(text):
    return text.decode('UTF-8')

cdef const char* pytoc(text):
    cdef const char* _text
    btext = text.encode('UTF-8')
    _text = btext
    return _text

cdef class Document:
    cdef document.Doc doc
    def __init__(self, json):
        self.doc = document.Doc(pytoc(json))

    cpdef change_json(self, val=None, amount=None, dictionary=None, valList=None, amountList=None, tupleList=None):
        if not val is None and not amount is None:
            self.doc.change(pytoc(val), amount)
        elif not dictionary is None:
            for item in dictionary:
                self.doc.change(pytoc(item), dictionary[item])
        elif not valList is None and not amountList is None:
            for i in range(len(valList)):
                self.doc.change(pytoc(valList[i]), amountList[i])
        elif not tupleList is None:
            for i in tupleList:
                self.doc.change(pytoc(i[0]), i[1])
        else:
            raise TypeError

    cpdef get_json(self):
        return ctopy(self.doc.get())
