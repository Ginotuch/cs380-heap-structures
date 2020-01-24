"""
Normal Graph:
----------
Generates a random fully connected graph to show the larger
average heap sizes. HeapQueue with tracking is on average
slower than without tracking because of dictionary access
time within the HeapQueue.swap method. Running a timing
profile on it shows that every method except HeapQueue.swap
is faster with tracking than without.


Bad Graph:
----------
This generates a specifically crafted graph and runs Dijkstra's
algorithm to traverse it. First using the new HeapQueue developed,
showing the average size of the heap and the amount of time it
takes. Then again with the standard library heapq implementation
which has a much larger heap size and takes much longer.

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
from misc.debug_versions.dijkstra import Dijkstra
from misc.debug_versions.dijkstra_heapqueue_no_tracking import Dijkstra as Dijkstra_no_tracking
from misc.debug_versions.dijkstra_heapq import Dijkstra as Dijkstra_heapq
from dijkstra.generate_graph import RandomConnectedGraph


def run_each_heap(graph):
    dijkstras = {
        "HeapQueue": Dijkstra,
        "HeapQueue no tracking": Dijkstra_no_tracking,
        "Heapq": Dijkstra_heapq
    }

    for name, d_object in dijkstras.items():
        print("Using", name)
        d = d_object(adj_list=graph.adj_list)
        t = time.time()
        d.start()
        print(" Average size of heap:", sum(d.sizes) / len(d.sizes))
        print(" Largest size of heap:", max(d.sizes))
        print(" Time taken:", str(round(time.time() - t, 2)) + "s\n")


def main_normal():
    print("Normal graph run")
    graph = RandomConnectedGraph(10 ** 5)
    graph.gen_graph()
    run_each_heap(graph)


def main_bad():
    print("Bad graph run")
    graph = RandomConnectedGraph(10 ** 5)
    graph.get_bad_graph()
    run_each_heap(graph)


main_normal()
main_bad()
