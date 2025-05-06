import time
import random

def quick_sort(arr):
    """
    Performs Quick Sort on a copy of the input list.
    Returns the sorted array, time taken, and operation count.
    """
    arr = arr.copy()
    operations = [0]
    start = time.time()

    _quick_sort(arr, 0, len(arr) - 1, operations)

    end = time.time()
    return arr, end - start, operations[0]

def _quick_sort(arr, low, high, operations):
    if low < high:
        # Partition the array and get the pivot index
        pi = _partition(arr, low, high, operations)

        # Recursively sort the two halves
        _quick_sort(arr, low, pi - 1, operations)
        _quick_sort(arr, pi + 1, high, operations)

def _partition(arr, low, high, operations):
    # Randomly choose pivot and swap it to the end
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        operations[0] += 1  # Comparison
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
            operations[0] += 1  # Swap operation

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to correct location
    operations[0] += 1
    return i + 1
