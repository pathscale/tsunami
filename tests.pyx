from wrappers.rapidjson cimport cdocument as cdoc
from libcpp.string cimport string
from libc.stdlib cimport malloc, free
from cython.parallel import parallel, prange
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

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

cdef const char* simple_test_Doc() nogil:
    cdef:
        cdoc.Doc *d
        const char* data = TEST_DATA
    d = new cdoc.Doc(data)
    result = d.get_json()
    del d
    return result


def run_simple_test():
    cdef:
        const char* result
    with nogil:
        result = simple_test_Doc()
    return result, "nogil test"


def run_worker_test(int n_cycles=1000, int n_workers = 4):
    cdef:
        int worker_run = int(n_cycles / n_workers)
    start_time = time.time()
    with nogil, parallel(num_threads=n_workers):
        parse_omp_worker(worker_run)
    elapsed = time.time() - start_time
    return elapsed


def parse_py_worker(int cycles):
    with nogil:
        for i in range(cycles):
            simple_test_Doc()


def construct_py_worker(int cycles):
    with nogil:
        for i in range(cycles):
            simple_test_Doc()


cdef void parse_omp_worker(int cycles) nogil:
    cdef:
        int i
    for i in range(cycles):
        simple_test_Doc()


def run_iteration_test(int n_cycles=1000, int iteration = 4):
    cdef:
        int worker_run = int(n_cycles / iteration)
        int i
    start_time = time.time()
    for i in range(iteration):
        parse_omp_worker(worker_run)
    elapsed = time.time() - start_time
    return elapsed


def run_threads_test(int n_cycles=1000, int n_workers = 4):
    cdef:
        int worker_run = int(n_cycles / n_workers)
    start_time = time.time()
    threads = []
    for i in range(n_workers):
        t = threading.Thread(target=parse_py_worker, args=[worker_run], daemon=True)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    elapsed = time.time() - start_time
    return elapsed


def test_construct_tpe(int n_cycles=1000, int n_workers=4):
    cdef:
        int worker_run = int(n_cycles / n_workers)
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        futures = []
        for i in range(n_workers):
            futures.append( executor.submit(parse_py_worker, worker_run) )
        as_completed(futures)
    elapsed = time.time() - start_time
    return elapsed


def test_prange_test(int n_cycles=1000, int n_workers = 4):
    cdef:
        int worker_run = int(n_cycles / n_workers)
        int i
    start_time = time.time()
    for i in prange(n_workers, nogil=True):
        parse_omp_worker(worker_run)
    elapsed = time.time() - start_time
    return elapsed
