import random  #for generating random array/list
import multiprocessing #for parallelism, cpu count, pool

def find_max(chunk):
    return max(chunk) #returns maximum element from list

def find_average(chunk):
    return sum(chunk) / len(chunk) #average

def parallel_reduction(data, operation):
    processes = multiprocessing.cpu_count() #number of CPUs available
    pool = multiprocessing.Pool(processes=processes) #Parallelism
    chunk_size = len(data) // processes 
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)] #list comprehension to create new list based on data
    results = pool.map(operation, chunks)
    pool.close() #closes pool / parallelism
    pool.join() #join parallely halved elements
    
    return operation(results)


if __name__ == '__main__':
    population = list(range(1, 100)) # 1 te 100 mdhlya kontya pn numbers
    sample_size = 8 #size of list
    data = random.sample(population, sample_size) #Random List
    print("Data:", data)
    
    max_value = parallel_reduction(data, find_max)
    print("Max value:", max_value)
    
    average = parallel_reduction(data, find_average)
    print("Average:", average)
    
    
    
    #In parallel reduction, the idea is to divide the input data into smaller chunks and distribute them among multiple processors or threads that can work simultaneously.
