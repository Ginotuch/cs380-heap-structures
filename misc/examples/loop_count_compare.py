"""
Shows a weird case of heapq requiring logn operations for siftup
even though it's not required.
"""
from misc.debug_versions.heapqueue import HeapQueue
import misc.debug_versions.heapq2 as heapq
import time
nodes = 2**20 - 2
a = [(1, 1) for x in range(nodes)]

my_heap = HeapQueue(a, duplicates=True)
print("Starting pop on HeapQueue")
t = time.time()
my_heap.heapify_down_loops = 0  # resets number of loops before pop
my_heap.pop()
print(" Time taken:", time.time() - t)
print(" heapifydown loops:", my_heap.heapify_down_loops)
print()

heapq.heapify(a)
heapq.p = True
print("Starting pop on heapq")
t = time.time()
heapq.heappop(a)
print("Time taken:", time.time() - t)
print(" heapifydown loops:", heapq.loops)