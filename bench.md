# bench test
up to 8 workers and 10000 cycles each, avarage from 10 loops

## parallel cython

Number of workers: 1	 Elapsed: 0.05 sec	4503 ns/op

Number of workers: 2	 Elapsed: 0.02 sec	2273 ns/op

Number of workers: 3	 Elapsed: 0.02 sec	1501 ns/op

Number of workers: 4	 Elapsed: 0.01 sec	1140 ns/op

Number of workers: 5	 Elapsed: 0.01 sec	910 ns/op

Number of workers: 6	 Elapsed: 0.01 sec	759 ns/op

Number of workers: 7	 Elapsed: 0.01 sec	639 ns/op

Number of workers: 8	 Elapsed: 0.01 sec	569 ns/op

## pythreads

Number of workers: 1	 Elapsed: 0.05 sec	4560 ns/op

Number of workers: 2	 Elapsed: 0.02 sec	2474 ns/op

Number of workers: 3	 Elapsed: 0.02 sec	1710 ns/op

Number of workers: 4	 Elapsed: 0.01 sec	1399 ns/op

Number of workers: 5	 Elapsed: 0.01 sec	1289 ns/op

Number of workers: 6	 Elapsed: 0.01 sec	1260 ns/op

Number of workers: 7	 Elapsed: 0.01 sec	1430 ns/op

Number of workers: 8	 Elapsed: 0.01 sec	1419 ns/op

## ThreadPoolExecutor

Number of workers: 1	 Elapsed: 0.05 sec	4800 ns/op

Number of workers: 2	 Elapsed: 0.03 sec	2729 ns/op

Number of workers: 3	 Elapsed: 0.02 sec	1880 ns/op

Number of workers: 4	 Elapsed: 0.01 sec	1479 ns/op

Number of workers: 5	 Elapsed: 0.01 sec	1370 ns/op

Number of workers: 6	 Elapsed: 0.01 sec	1260 ns/op

Number of workers: 7	 Elapsed: 0.01 sec	1310 ns/op

Number of workers: 8	 Elapsed: 0.01 sec	1359 ns/op

## iterations range()

Number of workers: 1	 Elapsed: 0.05 sec	4730 ns/op

Number of workers: 2	 Elapsed: 0.04 sec	4429 ns/op

Number of workers: 3	 Elapsed: 0.04 sec	4450 ns/op

Number of workers: 4	 Elapsed: 0.04 sec	4459 ns/op

Number of workers: 5	 Elapsed: 0.04 sec	4499 ns/op

Number of workers: 6	 Elapsed: 0.04 sec	4450 ns/op

Number of workers: 7	 Elapsed: 0.04 sec	4460 ns/op

Number of workers: 8	 Elapsed: 0.04 sec	4440 ns/op

## prange cython

Number of workers: 1	 Elapsed: 0.04 sec	4450 ns/op

Number of workers: 2	 Elapsed: 0.04 sec	4439 ns/op

Number of workers: 3	 Elapsed: 0.04 sec	4449 ns/op

Number of workers: 4	 Elapsed: 0.04 sec	4470 ns/op

Number of workers: 5	 Elapsed: 0.05 sec	4629 ns/op

Number of workers: 6	 Elapsed: 0.04 sec	4450 ns/op

Number of workers: 7	 Elapsed: 0.04 sec	4499 ns/op

Number of workers: 8	 Elapsed: 0.04 sec	4440 ns/op