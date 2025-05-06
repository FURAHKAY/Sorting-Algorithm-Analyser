import time

def selection_sort(arr):
    """
    Performs Selection Sort on a copy of the input list.
    Returns the sorted array, time taken, and operation count.
    """
    arr = arr.copy()     # Work on a copy to preserve original
    n = len(arr)
    operations = 0       # Count comparisons and swaps
    start = time.time()

    # Move boundary of unsorted subarray
    for i in range(n):
        min_idx = i

        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            operations += 1  # Comparison
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            operations += 1  # Swap operation

    end = time.time()
    return arr, end - start, operations
