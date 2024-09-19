import time 
from functools import lru_cache

# Maximum number of results to cache. When the cache limit is reached, the least recently used items are discarded.
@lru_cache(maxsize=128)
def expensive_function(x):
    """
    Simulates an expensive computation and caches the result.

    Args:
        x (int): The input value for the function.

    Returns:
        int: The square of the input value.

    The result is cached to optimize repeated calls with the same input,
    reducing computation time.
    
    Caching is done with a Least Recently Used (LRU) policy.
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