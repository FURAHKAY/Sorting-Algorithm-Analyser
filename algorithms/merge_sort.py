import time

def merge_sort(arr):
    """
    Performs Merge Sort on a copy of the input list.
    Returns the sorted array, time taken, and operation count.
    """
    arr = arr.copy()  # Preserve original
    operations = [0]  # Use list to make it mutable in recursive calls
    start = time.time()

    sorted_arr = _merge_sort(arr, operations)

    end = time.time()
    return sorted_arr, end - start, operations[0]

def _merge_sort(arr, operations):
    if len(arr) <= 1:
        return arr

    # Divide the array
    mid = len(arr) // 2
    left = _merge_sort(arr[:mid], operations)
    right = _merge_sort(arr[mid:], operations)

    # Conquer and merge the sorted halves
    return _merge(left, right, operations)

def _merge(left, right, operations):
    merged = []
    i = j = 0

    # Merge elements from both lists in sorted order
    while i < len(left) and j < len(right):
        operations[0] += 1  # Comparison
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
