import random
from math import inf

from heap import Heap
from generate_graph import RandomConnectedGraph


class Dijkstra:
    def __init__(self, node_count=100000):
        self.graph = RandomConnectedGraph(node_count)
        self.graph.gen_graph()
        self.adjacency_list = self.graph.adj_list
        self.pq = Heap()
        self.colour = [0] * len(self.adjacency_list)
        self.dist = [inf] * len(self.adjacency_list)
        self.white = 0
        self.grey = 1
        self.black = 2
        self.end_node = len(self.adjacency_list) - 1

    def start(self):
        self.pq.push(0, 0)
        while self.pq.size > 0:
            t1, u = self.pq.pop()

            if self.colour[u] == self.black:
                raise Exception("Something went wrong")

            if u == self.end_node:
                self.dist[u] = t1
                break

            for node in self.adjacency_list[u]:
                t2 = t1 + 1
                if self.colour[node] == self.white:
                    self.colour[node] = self.grey
                    self.pq.push(t2, node)
                elif self.colour[node] == self.grey and self.pq.get_key(node) > t2:
                    self.pq.push(t2, node)
            self.colour[u] = self.black
            self.dist[u] = t1
        print("Distance:", self.dist[self.end_node])


if __name__ == '__main__':
    d = Dijkstra()
    d.start()
    print()
