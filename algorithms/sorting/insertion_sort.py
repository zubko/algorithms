def insertion_sort(arr):
    """In-place insertion sort"""
    for i in range(1, len(arr)):
        j = i - 1
        current = arr[i]
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


# export
name = "insertion sort"
func = insertion_sort
limit = 25000

if __name__ == '__main__':
    def test_sort(arr):
        print(f"Array: {arr}")
        print(f"Sorted: {insertion_sort(arr)}")
        print("---------")

    test_sort([])
    test_sort([6, 3, 1, 2, 4, 6, 7, 2, 1, -5])
    test_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])  # worst case
