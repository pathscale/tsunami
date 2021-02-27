import pytest

from core import rapidjson as rj
from core import tests as tests

def bench_print_result(elapsed, n_workers, n_cycles):
    return ("\n\nNumber of workers: %s\t Elapsed: %.2f sec\t%.0d ns/op" % (n_workers, elapsed, (elapsed / n_cycles * 10 ** 9)))
def run_function_for_thread_test(function, name, n_cycles = 1000, n_workers_max=11 ):
    text = (f"\n\n## {name}")
    #text+=("\n################ Parsing ################")
    for n_workers in range(1, n_workers_max):
        elapsed = function(n_cycles, n_workers)
        text+=bench_print_result(elapsed, n_workers, n_cycles)
    return text

def threads_test():
    n_cycles = 10000
    max_workers = 8
    text =f"# bench test\nup to {max_workers} workers and {n_cycles} cycles each"
    text+=run_function_for_thread_test(function=tests.run_worker_test, name="parallel cython", n_cycles=n_cycles, n_workers_max=max_workers)
    text+=run_function_for_thread_test(function=tests.run_iteration_test, name="iterations range()", n_cycles=n_cycles, n_workers_max=max_workers)
    text+=run_function_for_thread_test(function=tests.run_threads_test, name="pythreads", n_cycles=n_cycles, n_workers_max=max_workers)
    text+=run_function_for_thread_test(function=tests.test_construct_tpe, name="ThreadPoolExecutor", n_cycles=n_cycles, n_workers_max=max_workers)
    text+=run_function_for_thread_test(function=tests.test_prange_test, name="prange cython", n_cycles=n_cycles, n_workers_max=max_workers)
    return text

if __name__ == '__main__':
    with open("bench.md", "w") as f:
        x = str(threads_test())
        f.write(x)