from multiprocessing import Pool

def worker_func(x):
    # Perform some computation
    result = x * x
    return result

if __name__ == '__main__':
    # Create a pool of processes
    with Pool() as pool:
        # Define the input data
        data = [1, 2, 3, 4, 5]

        # Apply the worker function to the data using the pool
        results = [pool.apply_async(worker_func, (x,)) for x in data]

        # Retrieve the return values from the async results
        output = [result.get() for result in results]

    # Print the results
    print(output)
