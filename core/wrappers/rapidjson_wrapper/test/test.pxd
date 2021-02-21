from libcpp cimport bool

cdef extern from "./test.h":
    int test(char* json)

    cppclass Doc:
        Doc() nogil
        Doc(char* json) nogil
        void Parse(char* json) nogil
        bool HasError() nogil
        char* GetError() nogil
        #~Doc()
