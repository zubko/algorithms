def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quicksort(less)+[pivot]+quicksort(greater)


print(quicksort([5, 3, 1, 3, 7, 9, 10, 6, 22, -5]))
