# bench test
up to 8 workers and 10000 cycles each

## parallel cython

Number of workers: 1	 Elapsed: 0.04 sec	4499 ns/op

Number of workers: 2	 Elapsed: 0.02 sec	2200 ns/op

Number of workers: 3	 Elapsed: 0.02 sec	1501 ns/op

Number of workers: 4	 Elapsed: 0.01 sec	1099 ns/op

Number of workers: 5	 Elapsed: 0.01 sec	900 ns/op

Number of workers: 6	 Elapsed: 0.01 sec	799 ns/op

Number of workers: 7	 Elapsed: 0.01 sec	600 ns/op

## iterations range()

Number of workers: 1	 Elapsed: 0.05 sec	4500 ns/op

Number of workers: 2	 Elapsed: 0.05 sec	4502 ns/op

Number of workers: 3	 Elapsed: 0.05 sec	4504 ns/op

Number of workers: 4	 Elapsed: 0.05 sec	4503 ns/op

Number of workers: 5	 Elapsed: 0.05 sec	4511 ns/op

Number of workers: 6	 Elapsed: 0.04 sec	4442 ns/op

Number of workers: 7	 Elapsed: 0.05 sec	4500 ns/op

## pythreads

Number of workers: 1	 Elapsed: 0.05 sec	4601 ns/op

Number of workers: 2	 Elapsed: 0.02 sec	2400 ns/op

Number of workers: 3	 Elapsed: 0.02 sec	1999 ns/op

Number of workers: 4	 Elapsed: 0.01 sec	1300 ns/op

Number of workers: 5	 Elapsed: 0.01 sec	1344 ns/op

Number of workers: 6	 Elapsed: 0.02 sec	1500 ns/op

Number of workers: 7	 Elapsed: 0.01 sec	1199 ns/op

## ThreadPoolExecutor

Number of workers: 1	 Elapsed: 0.05 sec	4899 ns/op

Number of workers: 2	 Elapsed: 0.02 sec	2399 ns/op

Number of workers: 3	 Elapsed: 0.02 sec	1800 ns/op

Number of workers: 4	 Elapsed: 0.01 sec	1399 ns/op

Number of workers: 5	 Elapsed: 0.01 sec	1200 ns/op

Number of workers: 6	 Elapsed: 0.01 sec	1099 ns/op

Number of workers: 7	 Elapsed: 0.01 sec	1200 ns/op

## prange cython

Number of workers: 1	 Elapsed: 0.04 sec	4499 ns/op

Number of workers: 2	 Elapsed: 0.04 sec	4400 ns/op

Number of workers: 3	 Elapsed: 0.05 sec	4500 ns/op

Number of workers: 4	 Elapsed: 0.04 sec	4399 ns/op

Number of workers: 5	 Elapsed: 0.04 sec	4499 ns/op

Number of workers: 6	 Elapsed: 0.05 sec	4500 ns/op

Number of workers: 7	 Elapsed: 0.04 sec	4499 ns/op