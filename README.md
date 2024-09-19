# Python Caching Techniques

Caching is a technique used to store results of expensive computations and reuse them to improve performance, especially for repeated operations. In Python, there are several ways to implement caching, including in-memory and disk-based caching.

## Key Concepts

### 1. **In-Memory Caching with `functools.lru_cache`**

- `lru_cache` (Least Recently Used Cache) is a decorator provided by the `functools` module.
- It caches results in memory and automatically discards the least recently used entries when the cache limit (`maxsize`) is reached.
- Great for optimizing functions that are called frequently with the same arguments.

### 2. **Persistent Caching with `diskcache`**

- `diskcache` allows caching on disk, enabling persistent caching that works across program executions.
- Useful when you want to retain cached results beyond the lifespan of your program, saving them to disk for later use.
- Cached items can be retrieved even after a program restarts, making it a reliable solution for large datasets or computations that should not be repeated.

### 3. **Benefits of Caching**

- **Performance Boost**: Avoids redundant computations by reusing previously computed results.
- **Optimized Resource Usage**: Reduces CPU usage for expensive operations, improving efficiency.
- **Disk-Based Caching**: Allows persistence of data across program runs, offering long-term efficiency.

## When to Use Caching?

- **Expensive Computations**: Functions that take significant time or resources to compute.
- **Repeated Calls**: Functions that are called multiple times with the same arguments.
- **Database Queries or API Calls**: Caching can reduce load by storing results of heavy database or external API requests.

## Caching Policies

- **LRU (Least Recently Used)**: The most common caching policy that discards the least recently used entries when the cache is full.
- **Max Size**: Defines the number of items that can be cached before older ones are discarded.

## Tools & Libraries

- `functools.lru_cache`: In-memory caching for Python functions.
- `diskcache`: Disk-based caching for persistent storage of cached results.

## Best Practices

- Set an appropriate `maxsize` for caches to balance memory usage and cache efficiency.
- Use disk-based caching for long-running applications or computations that should not be repeated.
- Monitor performance to ensure that caching is benefiting your use case, as caching can also consume resources.

## Summary

Caching is an essential optimization technique that helps reduce computation time by storing the results of expensive operations. In-memory caching with `lru_cache` is ideal for repeated function calls, while `diskcache` enables persistent caching across multiple program runs, providing flexibility and performance improvements.

