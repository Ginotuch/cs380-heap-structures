"""
This generates a graph and runs Dijkstra's algorithm to traverse it.
First using the new HeapQueue developed, showing the average size
of the heap and the amount of time it takes. Then again with the
standard library heapq implementation which has a much larger heap
size and takes much longer.

Example output with 10^6 nodes on an Intel i5-8250U (8 cores) @ 3.4GHz:
  > Using the new HeapQueue
  >  Average size of heap: 1.999998
  >  Time taken: 6.92s
  >
  > Using standard library heapq
  >  Average size of heap: 500000.499999
  >  Time taken: 15.89s
"""

import time
from misc.examples.dijkstra_example.dijkstra import Dijkstra
from misc.examples.dijkstra_example.dijkstra_heapqueue_no_tracking import Dijkstra as Dijkstra_no_tracking
from misc.examples.dijkstra_example.dijkstra_heapq import Dijkstra as Dijkstra_heapq
from dijkstra.generate_graph import RandomConnectedGraph

graph = RandomConnectedGraph(10 ** 6)
graph.get_bad_graph()

print("Using the new HeapQueue")
d = Dijkstra(adj_list=graph.adj_list)
t = time.time()
d.start()
print(" Time taken:", str(round(time.time() - t, 2)) + "s\n")

print("Using the new HeapQueue no tracking")
d = Dijkstra_no_tracking(adj_list=graph.adj_list)
t = time.time()
d.start()
print(" Time taken:", str(round(time.time() - t, 2)) + "s\n")

print("Using standard library heapq")
d = Dijkstra_heapq(adj_list=graph.adj_list)
t = time.time()
d.start()
print(" Time taken:", str(round(time.time() - t, 2)) + "s")
