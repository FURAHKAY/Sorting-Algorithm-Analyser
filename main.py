from utils import generate_test_data, measure_execution_time, plot_execution_times
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort

# Define sorting algorithms to test
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}

# Define input sizes to test
input_sizes = [100, 500, 1000, 2000, 4000]

# Dictionary to store performance results
results = {}

# Measure performance for each algorithm
for name, sort_func in algorithms.items():
    print(f"Running tests for: {name}")
    times = []
    for size in input_sizes:
        test_data = generate_test_data(size, array_type="random")
        elapsed = measure_execution_time(sort_func, test_data)
        times.append(elapsed)
        print(f"  Size: {size}, Time: {elapsed:.4f}s")
    results[name] = {"sizes": input_sizes, "times": times}

# Plot the results
plot_execution_times(results, title="Sorting Algorithm Time Complexity")
