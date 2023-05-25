import random
import multiprocessing

def find_max(chunk):
    return max(chunk)

def find_average(chunk):
    return sum(chunk) / len(chunk)

def parallel_reduction(data, operation):
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    chunk_size = len(data) // processes
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    results = pool.map(operation, chunks)
    pool.close()
    pool.join()
    
    return operation(results)


if __name__ == '__main__':
    population = list(range(1, 100))
    sample_size = 8
    data = random.sample(population, sample_size)
    print("Data:", data)
    
    max_value = parallel_reduction(data, find_max)
    print("Max value:", max_value)
    
    average = parallel_reduction(data, find_average)
    print("Average:", average)
