cdef extern from "wrap_document.h":
    # cdef const char* kekw(const char*, const char*, int)
    cppclass Doc:
        Doc(const char*) nogil
        Doc() nogil
        void set_int(const char*, int) nogil
        void set_string(const char*, const char*) nogil
        # void add_int(const char*, int) nogil
        int get_int(const char*) nogil
        const char* get_string(const char*) nogil
        const char* get_json() nogil
