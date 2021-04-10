def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


my_list = [1, 3, 6, 9, 13, 40, 200]
print binary_search(my_list, 40)
print binary_search(my_list, 5)
