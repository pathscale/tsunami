import pytest

from core import rapidjson as rj
from core import tests as tests

def bench_print_result(elapsed, n_workers, n_cycles):
    print("Number of workers: %s\t Elapsed: %.2f sec\t%.0d ns/op" % (n_workers, elapsed, (elapsed / n_cycles * 10 ** 9)))
def run_function_for_thread_test(function, name, n_cycles = 1000, n_workers_max=11 ):
    print(f"\n################ {name} ################")
    print("################ Parsing ################")
    for n_workers in range(1, n_workers_max):
        elapsed = function(n_cycles, n_workers)
        bench_print_result(elapsed, n_workers, n_cycles)

def threads_test():
    n_cycles = 10000
    max_workers = 12
    run_function_for_thread_test(function=tests.run_worker_test, name="parallel cython", n_cycles=n_cycles, n_workers_max=max_workers)
    run_function_for_thread_test(function=tests.run_iteration_test, name="iterations range()", n_cycles=n_cycles, n_workers_max=max_workers)
    run_function_for_thread_test(function=tests.run_threads_test, name="pythreads", n_cycles=n_cycles, n_workers_max=max_workers)
    run_function_for_thread_test(function=tests.test_construct_tpe, name="ThreadPoolExecutor", n_cycles=n_cycles, n_workers_max=max_workers)
    run_function_for_thread_test(function=tests.test_prange_test, name="prange cython", n_cycles=n_cycles, n_workers_max=max_workers)

if __name__ == '__main__':
    threads_test()