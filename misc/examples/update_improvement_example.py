"""
Shows the difference in performance between updating a single
node's priority repeatedly in HeapQueue versus heapq.

Updating priorities is not supported in heapq, so to get the
same functionality as with HeapQueue duplicate nodes must be
pushed onto the heap with lower priorities than the previously
added node. Then in a real application when popping from the
heapq's heap, all duplicate values have to be skipped over,
causing pop()'s runtime to worsen from O(logn) to O(mlog(n + m)
where m is the number of updates done to all nodes so far.
This also means that pushing onto the heap is slower which
changes the runtime of push() from O(logn) to O(log(n + m)).

This causes a large amount of memory usage, and much slower
pushes onto the heap because of all the duplicate nodes that a
new one must traverse up through to get to the root.

Example output with 10^7 updates on an Intel i5-8250U (8 cores) @ 3.4GHz:
  > Before anything RAM usage: 12.34MB
  >
  > Starting HeapQueue
  >  Heap size: 1
  >  Time taken: 6.36s
  >  After HeapQueue RAM usage: 12.34MB
  >
  > Starting heapq
  >  Heap size: 10000001
  >  Time taken: 45.66s
  >  After heapq RAM usage: 1067.94MB
"""

from heaps import HeapQueue, heapq2
import time
import os
import psutil

process = psutil.Process(os.getpid())


def mem():
    return "RAM usage: " + str(round(process.memory_info().rss * 1e-6, 2)) + "MB"


print("Before anything", mem(), "\n")

node_value = 0
updates = 10 ** 7

print("Starting HeapQueue")
h = HeapQueue()
h.push(0.5, node_value)
t = time.time()
for x in range(updates, 0, -1):
    h.push(x, node_value)
print(" Heap size:", h.size)
print(" Time taken:", str(round(time.time() - t, 2)) + "s")

print(" After HeapQueue", mem(), "\n")
h.peek()  # just to avoid garbage collector
h = None

print("Starting heapq")
hq = []
heapq2.heappush(hq, (0.5, node_value))
t = time.time()
for x in range(updates, 0, -1):
    heapq2.heappush(hq, (x, node_value))
print(" Heap size:", len(hq))
print(" Time taken:", str(round(time.time() - t, 2)) + "s")

print(" After heapq", mem())
hq[0] = 0  # just to avoid garbage collector
