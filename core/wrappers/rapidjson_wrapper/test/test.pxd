from libcpp cimport bool

cdef extern from "./test.h":
    int test(char* json)

    cppclass Doc:
        Doc()
        Doc(char* json)
        bool HasError()
        char* GetError()
        #~Doc()
