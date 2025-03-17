Solu.1   def max_weight_independent_set(weights):
    if not weights:
        return 0  # Edge case: empty list
    if len(weights) == 1:
        return weights[0]  # Edge case: single element

    # Step 1: Create a DP array
    dp = [0] * len(weights)

    # Step 2: Base cases
    dp[0] = weights[0]  # The first element must be taken
    dp[1] = max(weights[0], weights[1])  # Choose max of first two elements

    # Step 3: Fill the DP array using the recurrence relation
    for i in range(2, len(weights)):
        dp[i] = max(dp[i-1], dp[i-2] + weights[i])

    return dp[-1]  # The last element contains the result

# Example 
weights = [1, 2, 9, 4, 5, 0, 4]
print(max_weight_independent_set(weights))  # Output: 13

---------------------------------------------------------------------------------------------------------------------------------------------------------------

Solu2:   import heapq
def k_way_merge(lists, comparator):
    heap = []
    
    # Add first elements of each list into the heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (value, list index, element index)
    
    result = []
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Add next element from the same list
        if elem_idx + 1 < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1))
    
    return result

# Example Usage
lists = [[(1, 'a'), (3, 'b')], [(2, 'c'), (4, 'd')], [(0, 'e')]]
comparator = lambda x, y: x[0] - y[0]
print(k_way_merge(lists, comparator))  
# Output: [(0, 'e'), (1, 'a'), (2, 'c'), (3, 'b'), (4, 'd')]

---------------------------------------------------------------------------------------------------------------------------------------------------------------
Solu3:  import asyncio
import time
from collections import deque
import threading

class RateLimiter:
    def __init__(self, requests_per_second):
        self.capacity = requests_per_second
        self.tokens = self.capacity
        self.last_refill_time = time.monotonic()
        self.lock = threading.Lock()

    async def __aenter__(self):
        while True:
            with self.lock:
                now = time.monotonic()
                elapsed = now - self.last_refill_time
                self.tokens = min(self.capacity, self.tokens + elapsed * self.capacity)
                self.last_refill_time = now

                if self.tokens >= 1:
                    self.tokens -= 1
                    return
                
            await asyncio.sleep(0.1)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

# Example Usage
async def request():
    async with RateLimiter(requests_per_second=10):
        print("Request processed", time.time())

async def main():
    tasks = [request() for _ in range(20)]
    await asyncio.gather(*tasks)

asyncio.run(main())

---------------------------------------------------------------------------------------------------------------------------------------------------------------

Solu4: class Descriptor:
    def __init__(self, type_, validator, transformer=None):
        self.type_ = type_
        self.validator = validator
        self.transformer = transformer if transformer else lambda x: x
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, None)

    def __set__(self, instance, value):
        if not isinstance(value, self.type_):
            raise TypeError(f"Expected {self.type_}, got {type(value)}")

        if not self.validator(value):
            raise ValueError(f"Validation failed for value: {value}")

        self.data[instance] = self.transformer(value)

# Example Usage
class Product:
    price = Descriptor(float, lambda x: x > 0)
    name = Descriptor(str, lambda x: len(x) > 0, lambda x: x.upper())

    def __init__(self, name, price):
        self.name = name
        self.price = price

# Testing the descriptor
p = Product("laptop", 999.99)
print(p.name)  # Output: LAPTOP
print(p.price)  # Output: 999.99

# Invalid case
try:
    p.price = -5  # Should raise ValueError
except ValueError as e:
    print(e)

---------------------------------------------------------------------------------------------------------------------------------------------------------------



