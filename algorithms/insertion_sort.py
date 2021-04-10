def insertion_sorted(array):
    local_arr = array.copy()
    for i in range(1, len(local_arr)):
        j = i - 1
        current = local_arr[i]
        while j >= 0 and current < local_arr[j]:
            local_arr[j + 1] = local_arr[j]
            j -= 1
        local_arr[j + 1] = current
    return local_arr


def test_sort(arr):
    print(f"Array: {arr}")
    print(f"Sorted: {insertion_sorted(arr)}")
    print("---------")


test_sort([])
test_sort([6, 3, 1, 2, 4, 6, 7, 2, 1, -5])
test_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])  # worst case
