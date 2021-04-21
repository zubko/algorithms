def quicksort(arr):
    """Super short code of quicksort"""
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


# export
name = "quicksort super short"
func = quicksort


# test
if __name__ == "__main__":
    def test_sort(arr):
        print(f"Array: {arr}")
        print(f"Sorted: {quicksort(arr)}")
        print("---------")

    test_sort([5, 3, 1, 3, 7, 9, 10, 6, 22, -5])
