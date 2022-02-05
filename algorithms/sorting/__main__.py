# the runner to compare the performance of the different sorting algorithms

import random
import timeit

# importing sorting algorithms
# each one should have
#   name - a name of the algorithm
#   func - a sorting function which takes an array and returns a sorted one (it can be inplace sorting or pure func)
#   limit - (optional) a limit of size of array, running the algorithm beyond which is not reasonable for the tests
import quicksort_inplace
import quicksort_inplace_nonrec
import quicksort_super_short
import quicksort_inplace_with_insertion
import heap_sort
import default_sort
import insertion_sort
import merge_sort

modules = [
    default_sort,
    quicksort_super_short,
    quicksort_inplace,
    quicksort_inplace_nonrec,
    quicksort_inplace_with_insertion,
    heap_sort,
    insertion_sort,
    merge_sort
]


def test_correct(n):
    arr_unsorted = [random.randint(-1000000, +1000000) for i in range(n)]
    arr_sorted = sorted(arr_unsorted)
    for module in modules:
        if hasattr(module, 'limit') and n > module.limit:
            print(f"Skipping check with {n} elements for \"{module.name}\"")
        else:
            result = module.func(arr_unsorted.copy())
            is_correct = result == arr_sorted
            print(f"Test correct with {n} elements for \"{module.name}\": {is_correct}")
            assert is_correct, f"The sorting function of \"{module.name}\" returned incorrect result"


def test_run_time(n):
    arr = [random.randint(-1000000, +1000000) for i in range(n)]
    for module in modules:
        if hasattr(module, 'limit') and n > module.limit:
            print(f"{n}: {module.name}: skip")
        else:
            copy = arr.copy()
            time = timeit.timeit(lambda: module.func(copy), number=1)
            print(f"{n}: {module.name}: {time}")


test_correct(25_000)
test_correct(100_000)

# Super casual test of the growth of time with the growth of instance

test_run_time(25_000)
test_run_time(50_000)
test_run_time(100_000)
test_run_time(200_000)
test_run_time(400_000)
test_run_time(800_000)
test_run_time(1_600_000)
