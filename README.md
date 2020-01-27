# CS380 Heap Structures Research
Packages developed during research of heap structure implementations
 in python for CS380 at the University of Auckland.

## HeapQueue
A heap based priority queue implementation to demonstrate improvements
 over the standard Python library heapq by tracking element positions
 using a dictionary.
 
Feature improvements:
* *O(1)* lookup of any value's current priority with *HeapQueue.get_priority(value)*
* *O(logn)* modification of the priority for any value already in the heap
* *O(logn)* arbitrary element deletion with *HeapQueue.remove(value)*

_Note: Although better asymptotic worst cases than standard the library, HeapQueue will
be slower in most real world applications because of abstraction overhead and not
 currently having a C implementation._

## dijkstra package
An implementation of the dijkstra path finding algorithm as an example
 application for HeapQueue.

## heapq2.py
This is the standard heap based priority queue library with the C importing
 removed. Used to better compare speeds/operations with the custom HeapQueue
 class.

## myheapq.py
A better implementation of the _siftup function from heapq. The standard _siftup
 implementation in heapq does many unneeded operations which this version
 shows is not needed.

---
### Requirements
Developed for and tested with Python 3.8