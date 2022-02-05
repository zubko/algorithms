def merge_sort(arr):
    # sort 2 parts in new buffers
    # merge these 2 parts into the current array

    def merge(a1, a2):
        # we need 2 indexes
        # increase indexes
        i, j = 0, 0
        r = []
        while i < len(a1) or j < len(a2):
            if (j >= len(a2)) or (i < len(a1) and a1[i] < a2[j]):
                r.append(a1[i])
                i += 1
            else:
                r.append(a2[j])
                j += 1
        return r

    def sort_step(arr, left, right):
        if (right - left < 0):
            return []
        elif (right - left == 0):
            return [arr[left]]
        elif right - left == 1:
            if arr[left] < arr[right]:
                return [arr[left], arr[right]]
            else:
                return [arr[right], arr[left]]
        else:
            a1 = sort_step(arr, left, (right+left) // 2)
            a2 = sort_step(arr, (right+left) // 2 + 1, right)
            return merge(a1, a2)

    return sort_step(arr, 0, len(arr)-1)

print(merge_sort([12, 14, 9, 5, 2, 0, -5, 34, 3]))

name="Merge sort"
func=merge_sort

