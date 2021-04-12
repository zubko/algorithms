# Heap sort recursive algorithm
# src: Algorithms in a Nutshell, 2nd ed

import random
import timeit


def heap_sorted(source):
    arr = source.copy()
    n = len(arr)

    def heapify(i, max_i):
        left = i * 2 + 1
        right = i * 2 + 2
        top = i
        if left < max_i and arr[left] > arr[top]:
            top = left
        if right < max_i and arr[right] > arr[top]:
            top = right
        if top != i:
            arr[i], arr[top] = arr[top], arr[i]
            heapify(top, max_i)

    def build_heap():
        for i in reversed(range(0, n // 2)):
            heapify(i, n)

    def sort_heap():
        for i in reversed(range(1, n)):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(0, i)

    build_heap()
    sort_heap()
    return arr


def test_sort(arr):
    print(f"Array: {arr}")
    print(f"Sorted: {heap_sorted(arr)}")
    print("---------")


test_sort([])
test_sort([0, 6, 3, 1, 2, 12, 4, 10, 6, 20, 7, 2, 18, 1, -5])


# Super casual test of the growth of time with the growth of instance


def test_run_time(n):
    arr = [random.randint(-1000000, +1000000) for i in range(n)]
    print(f"Time of {n} is: {timeit.timeit(lambda: heap_sorted(arr), number=1)}")


test_run_time(100000)
test_run_time(200000)
test_run_time(400000)
test_run_time(800000)
