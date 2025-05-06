import time
import matplotlib.pyplot as plt
import random


def measure_execution_time(sort_func, array):
    """
    Measures how long it takes for sort_func to sort the array.
    Returns the elapsed time in seconds.
    """
    start_time = time.time()
    sort_func(array.copy())  # Use a copy to avoid modifying original
    end_time = time.time()
    return end_time - start_time


def generate_test_data(size, array_type="random"):
    """
    Generates an array of a given size and type.
    Types: 'random', 'sorted', 'reversed'
    """
    if array_type == "random":
        return [random.randint(1, 1000) for _ in range(size)]
    elif array_type == "sorted":
        return list(range(1, size + 1))
    elif array_type == "reversed":
        return list(range(size, 0, -1))
    else:
        raise ValueError("Invalid array_type: choose 'random', 'sorted', or 'reversed'.")


def plot_execution_times(results, title="Sorting Algorithm Performance"):
    """
    Plots a comparison graph of execution times.
    Input: results = { 'Bubble Sort': {'sizes': [...], 'times': [...]}, ... }
    """
    for name, data in results.items():
        plt.plot(data['sizes'], data['times'], label=name)

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
