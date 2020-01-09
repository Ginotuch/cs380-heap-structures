# CS380 Heap Structures Research
Packages developed during research of heap structure implementations
 in python for CS380 at the University of Auckland.

## HeapQueue
A heap based priority queue implementation to demonstrate improvements
 over the standard Python library heapq by tracking element positions
 using a dictionary.
 
Feature improvements:
* *O(1)* lookup of any value's current priority with *HeapQueue.get_key(value)*
* Ability to modify the priority of any value in the heap in *O(logn)* time
* *O(logn)* arbitrary element deletion with *HeapQueue.remove(value)*

## dijkstra package
An implementation of the dijkstra path finding algorithm as an example
 application for HeapQueue.

---
### Requirements
Developed for and tested with Python 3.8