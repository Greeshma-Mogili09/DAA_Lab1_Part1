import time
import matplotlib.pyplot as plt

def iterative_sum(N):
    result = 0
    for i in range(1, N+1):
        result += i
    return result

def recursive_sum(N):
    if N == 0:
        return 0
    return N + recursive_sum(N-1)

def plot_time_taken(N_values, iterative_times, recursive_times):
    plt.figure(figsize=(10, 6))
    plt.plot(N_values, iterative_times, marker='o', color='blue', label='Iterative')
    plt.plot(N_values, recursive_times, marker='o', color='red', label='Recursive')
    plt.xlabel('N')
    plt.ylabel('Time (seconds)')
    plt.title('Time taken to calculate sum of first N natural numbers')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

N_values = []
iterative_times = []
recursive_times = []


for N in range(1, 1001, 50):  
    N_values.append(N)
    
    start_time = time.time()
    iterative_sum(N)
    iterative_execution_time = time.time() - start_time
    iterative_times.append(iterative_execution_time)
    
    start_time = time.time()
    recursive_sum(N)
    recursive_execution_time = time.time() - start_time
    recursive_times.append(recursive_execution_time)

plot_time_taken(N_values, iterative_times, recursive_times)
