import time
from misc.debug_versions.dijkstra import Dijkstra
from misc.debug_versions.dijkstra_heapqueue_no_tracking import Dijkstra as Dijkstra_no_tracking
from misc.debug_versions.dijkstra_heapq import Dijkstra as Dijkstra_heapq
from dijkstra.generate_graph import RandomConnectedGraph


graph = RandomConnectedGraph(10 ** 6)
graph.gen_graph()

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
