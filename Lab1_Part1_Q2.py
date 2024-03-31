import random
import time
import matplotlib.pyplot as plt

def linear_search(arr, key):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == key:
            end_time = time.time()
            return end_time - start_time
    end_time = time.time()
    return end_time - start_time

def binary_search(arr, key):
    start_time = time.time()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            end_time = time.time()
            return end_time - start_time
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    end_time = time.time()
    return end_time - start_time

def plot_search_times(linear_times, binary_times):
    searches = range(1, 6)
    plt.figure(figsize=(10, 6))
    plt.plot(searches, linear_times, marker='o', color='blue', label='Linear Search')
    plt.plot(searches, binary_times, marker='o', color='red', label='Binary Search')
    plt.xlabel('Search')
    plt.ylabel('Time (seconds)')
    plt.title('Time taken by Linear and Binary Search for 5 different searches')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

arr = [random.randint(1, 1000) for _ in range(10000)]


linear_times = []
binary_times = []

for _ in range(5):
    search_key = int(input("Enter the search key: "))
    
    
    linear_times.append(linear_search(arr, search_key))
    
    
    sorted_arr = sorted(arr)
    binary_times.append(binary_search(sorted_arr, search_key))

plot_search_times(linear_times, binary_times)
