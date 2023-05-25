import random
import multiprocessing

def find_min(chunk):
    return min(chunk)

def calculate_sum(chunk):
    return sum(chunk)

def parallel_reduction(data, operation):
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    chunk_size = len(data) // processes
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    results = pool.map(operation, chunks)
    pool.close()
    pool.join()
    
    return operation(results)

# Example usage:
if __name__ == '__main__':
    population = list(range(1, 100))
    sample_size = 8
    data = random.sample(population, sample_size)
    print("Data:", data)
    
    min_value = parallel_reduction(data, find_min)
    print("Min value:", min_value)
    
    total_sum = parallel_reduction(data, calculate_sum)
    print("Sum:", total_sum)
