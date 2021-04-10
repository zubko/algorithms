def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0]+sum(arr[1:])


print(sum([1, 2, 3, 4, 5]))


def count(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1+count(arr[1:])


print(count([1, 2, 3, 4, 5, 6, 7]))


def binary_search(arr, item):
    def rec(a, b):
        if a > b:
            return None
        mid = (a + b) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            return rec(mid+1, b)
        else:
            return rec(a, mid-1)
    return rec(0, len(arr)-1)


arr = [1, 5, 9, 20, 40, 55, 77]
for i in arr:
    print(binary_search(arr, i))
print(binary_search(arr, 100))
