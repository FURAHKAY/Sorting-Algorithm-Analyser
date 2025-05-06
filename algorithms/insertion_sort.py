import time

def insertion_sort(arr):
    """
    Performs Insertion Sort on a copy of the input list.
    Returns the sorted array, time taken, and operation count.
    """
    arr = arr.copy()  # Avoid modifying the original input
    n = len(arr)
    operations = 0     # Track number of comparisons and shifts
    start = time.time()

    # Traverse from the second element to the end
    for i in range(1, n):
        key = arr[i]  # Element to be inserted into sorted portion
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element
            j -= 1
            operations += 1      # Count comparison/shift

        arr[j + 1] = key  # Insert the key at the correct position
        operations += 1   # For insertion

    end = time.time()
    return arr, end - start, operations
