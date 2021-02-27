from libcpp.string cimport string
from libc.stdlib cimport malloc, free
from libcpp cimport bool

#from ..wrappers.rapidjson_wrapper cimport rjson_wrapper as rjw
from ..wrappers.rapidjson_wrapper.test cimport test as t
from ..wrappers.utils cimport utils

cdef string TEST_RAW = b"""{
    "method": 10000,
    "seq": 3,
    "params": {
      "test_param_1": false,
      "test_param_2": null,
      "test_param_3": "what",
      "test_param_4": 4,
      "test_param_5": [
        1111,
        2222,
        3333
      ],
      "test_param_6": [
        false,
        true,
        false
      ],
      "test_param_7": [
        "aaa",
        "bbb",
        "ccc"
      ],
      "test_param_8": {
        "sub_param_1": 1,
        "sub_param_2": "blah",
        "nested_sub_param": {
          "nested1": "nested",
          "nested2": 1,
          "nestedList": [1, 2, 3]
        }
      }
    }
}"""

cdef const char *TEST_DATA = TEST_RAW.c_str()

cdef bool simple_test_Doc() nogil:
    cdef:
        t.Doc *d
        char* data = utils.constCharToChar(TEST_DATA)
    d = new t.Doc()
    d.Parse(data)

    #cdef char * error = utils.btoc(d.HasError())
    #utils.cprint(error)
    return d.HasError()

def run_simple_test():
    cdef:
        bool result
    with nogil:
        result = simple_test_Doc()
    return result, "nogil test"