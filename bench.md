# bench test
up to 8 workers and 10000 cycles each

## parallel cython

Number of workers: 1	 Elapsed: 0.04 sec	4499 ns/op

Number of workers: 2	 Elapsed: 0.02 sec	2256 ns/op

Number of workers: 3	 Elapsed: 0.02 sec	1500 ns/op

Number of workers: 4	 Elapsed: 0.01 sec	1100 ns/op

Number of workers: 5	 Elapsed: 0.01 sec	899 ns/op

Number of workers: 6	 Elapsed: 0.01 sec	799 ns/op

Number of workers: 7	 Elapsed: 0.01 sec	600 ns/op

Number of workers: 8	 Elapsed: 0.01 sec	599 ns/op

## iterations range()

Number of workers: 1	 Elapsed: 0.05 sec	4500 ns/op

Number of workers: 2	 Elapsed: 0.05 sec	4600 ns/op

Number of workers: 3	 Elapsed: 0.05 sec	4699 ns/op

Number of workers: 4	 Elapsed: 0.05 sec	4599 ns/op

Number of workers: 5	 Elapsed: 0.05 sec	4500 ns/op

Number of workers: 6	 Elapsed: 0.05 sec	4599 ns/op

Number of workers: 7	 Elapsed: 0.05 sec	4500 ns/op

Number of workers: 8	 Elapsed: 0.04 sec	4499 ns/op

## pythreads

Number of workers: 1	 Elapsed: 0.05 sec	5200 ns/op

Number of workers: 2	 Elapsed: 0.02 sec	2499 ns/op

Number of workers: 3	 Elapsed: 0.02 sec	1800 ns/op

Number of workers: 4	 Elapsed: 0.02 sec	1600 ns/op

Number of workers: 5	 Elapsed: 0.01 sec	1299 ns/op

Number of workers: 6	 Elapsed: 0.02 sec	1500 ns/op

Number of workers: 7	 Elapsed: 0.02 sec	1500 ns/op

Number of workers: 8	 Elapsed: 0.01 sec	1300 ns/op

## ThreadPoolExecutor

Number of workers: 1	 Elapsed: 0.05 sec	4599 ns/op

Number of workers: 2	 Elapsed: 0.02 sec	2499 ns/op

Number of workers: 3	 Elapsed: 0.02 sec	1900 ns/op

Number of workers: 4	 Elapsed: 0.01 sec	1499 ns/op

Number of workers: 5	 Elapsed: 0.01 sec	1300 ns/op

Number of workers: 6	 Elapsed: 0.01 sec	1199 ns/op

Number of workers: 7	 Elapsed: 0.01 sec	1400 ns/op

Number of workers: 8	 Elapsed: 0.02 sec	1500 ns/op

## prange cython

Number of workers: 1	 Elapsed: 0.04 sec	4499 ns/op

Number of workers: 2	 Elapsed: 0.05 sec	4600 ns/op

Number of workers: 3	 Elapsed: 0.04 sec	4499 ns/op

Number of workers: 4	 Elapsed: 0.04 sec	4499 ns/op

Number of workers: 5	 Elapsed: 0.05 sec	4600 ns/op

Number of workers: 6	 Elapsed: 0.05 sec	4500 ns/op

Number of workers: 7	 Elapsed: 0.05 sec	4599 ns/op

Number of workers: 8	 Elapsed: 0.05 sec	4500 ns/op