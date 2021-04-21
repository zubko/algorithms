# src: Algorithms in a Nutshell, 2nd ed

def quicksort(arr):
    """Inplace sorting with quick sort"""
    def partition(left, right, pivot_index):
        pivot = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        last_left_part = left
        for idx in range(left, right):
            if arr[idx] <= pivot:
                arr[idx], arr[last_left_part] = arr[last_left_part], arr[idx]
                last_left_part += 1
        arr[right], arr[last_left_part] = arr[last_left_part], arr[right]
        return last_left_part

    def step(left, right):
        if right <= left:
            return
        pivot_index = partition(left, right, left)
        step(left, pivot_index-1)
        step(pivot_index+1, right)

    step(0, len(arr)-1)
    return arr


# export
name = "quicksort inplace"
func = quicksort


# test
if __name__ == "__main__":
    def test_sort(arr):
        print(f"Array: {arr}")
        print(f"Sorted: {quicksort(arr)}")
        print("---------")

    test_sort([5, 3, 1, 3, 7, 9, 10, 6, 22, -5])
