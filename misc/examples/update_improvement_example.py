"""
Shows the difference in performance between updating a single
node's priority repeatedly in HeapQueue versus heapq.

Updating priorities is not supported in heapq, so to get the
same functionality as with HeapQueue duplicate nodes must be
pushed onto the heap with lower priorities than the previously
added node. Then in a real application when popping from the
heapq's heap, all duplicate values have to be skipped over,
causing pop()'s worstcase runtime to grow from Omega(logn) to
Omega(mlog(n + m) where m is the number of updates done to all
nodes so far. This also means that pushing onto the heap is
slower which changes the worstcase runtime of push() from
Omega(logn) to Omega(log(n + m)).

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
import time
from misc.debug_versions.util import mem
from typing import List
from heaps.wrappers import HeapWrapper, HeapQueueWrapped, HeapqWrapped


def f() -> List[HeapWrapper]:
    return [
        HeapQueueWrapped(name="HeapQueue"),
        HeapQueueWrapped(name="HeapQueue with duplicates", duplicates=True),
        HeapqWrapped(name="Heapq")
    ]


print("Before anything", mem(), "\n")

node_value = 0

for power in range(1, 7 + 1):
    updates: int = 10 ** power
    print()
    print("=" * 15)
    print("Updates: 10^{:d}".format(power))
    print("=" * 15)
    for heap_i, heap in enumerate((heaps := f())):
        t = time.time()
        print("Starting {} \ncurrent {}".format(heap.name, mem()))
        heap.push(0.5, node_value)
        for x in range(updates, 0, -1):
            heap.push(x, node_value)
        print(" Heap size:", heap.size())
        print(" Time taken:", str(round(time.time() - t, 2)) + "s")
        print(" After", heap.name, mem(), "\n")
        heap.peek()  # avoid garbage collector before memory check
        heaps[heap_i] = None  # induce garbage collector to clear memory
