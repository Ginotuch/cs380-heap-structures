import time
from dijkstra_example.dijkstra import Dijkstra
from dijkstra_example.dijkstra_heapq import Dijkstra as Dijkstra_heapq
from dijkstra.generate_graph import  RandomConnectedGraph

graph = RandomConnectedGraph(10**5)
graph.get_bad_graph()

d = Dijkstra(adj_list=graph.adj_list)
t = time.time()
d.start()
print(time.time() - t)


d = Dijkstra_heapq(adj_list=graph.adj_list)
t = time.time()
d.start()
print(time.time() - t)
