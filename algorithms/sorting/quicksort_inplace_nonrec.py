# src: Algorithms in a Nutshell, 2nd ed

def quicksort(arr):
    """Inplace sorting with quick sort without recursion"""

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

    queue = [(0, len(arr) - 1)]
    queue_index = 0

    def step(index):
        left, right = queue[index]
        pivot_index = partition(left, right, left)
        if left < pivot_index - 1:
            queue.append((left, pivot_index - 1))
        if pivot_index + 1 < right:
            queue.append((pivot_index + 1, right))

    while queue_index < len(queue):
        step(queue_index)
        queue_index += 1

    return arr


# export
name = "quicksort inplace (non-recursive)"
func = quicksort

# test
if __name__ == "__main__":
    def test_sort(arr):
        print(f"Array: {arr}")
        print(f"Sorted: {quicksort(arr)}")
        print("---------")


    test_sort([5, 3, 1, 3, 7, 9, 10, 6, 22, -5])
