cdef extern from "test.h":
    # cdef const char* kekw(const char*, const char*, int)
    cppclass Doc:
        Doc(const char*)
        Doc()
        void change(const char*, int)
        const char* get()
