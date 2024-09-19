import diskcache as dc 
import time 

# Initialize a disk-based cache stored in the 'cache_dir' directory.
cache = dc.Cache('./cache_dir')

@cache.memoize()
def expensive_function(x):
    """
    Simulates an expensive computation and caches the result to disk.

    Args:
        x (int): The input value for the function.

    Returns:
        int: The square of the input value.

    The result is cached and persisted on disk using diskcache. 
    This enables retrieval of the cached result even across different runs of the program.
    
    Caching is especially useful for functions that are computationally expensive,
    as it reduces redundant computations and improves performance.
    """
    print(f"Computing {x}")
    sum = 0
    for i in range(x):
        sum += i 
    return sum

# First function call before cache
start_time = time.time()
print(expensive_function(65))
final_time = (time.time() - start_time)
print(f"Overall time to compute: {final_time:.6f} seconds")

# Function call after cache
start_time = time.time()
print(expensive_function(65))
final_time = (time.time() - start_time)
print(f"Overall time to retrieve from cache: {final_time:.6f} seconds")