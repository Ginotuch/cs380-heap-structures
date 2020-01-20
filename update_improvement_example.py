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
