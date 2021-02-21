from libcpp cimport bool
cimport libcpp.string

cpdef char* _chars(str pystring)
cpdef str _text(char* charstr)

cdef extern from "cpputils.hpp":
    void cprint(char *s) nogil
    char* btoc(bool val) nogil
    char* itoc(int val) nogil
    char* constCharToChar(const char * string) nogil