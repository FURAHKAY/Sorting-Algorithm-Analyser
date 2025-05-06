import time

def bubble_sort(arr):
    """
    Performs Bubble Sort on a copy of the input list.
    Returns the sorted array, time taken, and operation count.
    """
    n = len(arr)
    arr = arr.copy()  # Make a copy to avoid mutating original input
    operations = 0     # Track comparisons and swaps
    start = time.time()

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so skip them
        for j in range(0, n - i - 1):
            operations += 1  # Comparison
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                operations += 1  # Swap

    end = time.time()
    return arr, end - start, operations
