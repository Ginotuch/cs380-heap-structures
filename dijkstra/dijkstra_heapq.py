from math import inf
from typing import List, Tuple, Union

import heaps.heapq2 as heapq
from dijkstra.generate_graph import RandomConnectedGraph


class Dijkstra:
    Distance = Union[int, float]

    def __init__(self, node_count=100000, adj_list=None):
        self.adjacency_list: List[List[Tuple[Dijkstra.Distance, int]]] = adj_list
        if adj_list is None:
            self.graph = RandomConnectedGraph(node_count)
            self.graph.gen_graph()
            self.adjacency_list = self.graph.adj_list
        self.pq: List = []
        self.colour: List[int] = [0] * len(self.adjacency_list)
        self.dist: List[Dijkstra.Distance] = [inf] * len(self.adjacency_list)
        self.white = 0  # Unexplored nodes
        self.grey = 1  # Partially explored nodes (shortest path not yet known)
        self.black = 2  # Fully explored nodes (shortest path known)
        self.end_node: int = len(self.adjacency_list) - 1

    def start(self):
        heapq.heappush(self.pq, (0, 0))  # Pushing source node 's' to queue. Distance to itself is 0
        while self.pq:
            t1, u = heapq.heappop(self.pq)  # 't1' = cost from 's' to 'u'

            if self.colour[u] == self.black:
                continue

            if u == self.end_node:  # If 'u' is the desired node, then we have already found the shortest path
                self.dist[u] = t1
                break

            for node, cost in self.adjacency_list[u]:

                # 'cost' is dist('u', 'node')
                # 't2' is dist('s', 'u') + dist('u', 'node'). (path to 'node' through 'u')
                t2: Dijkstra.Distance = t1 + cost

                if self.colour[node] == self.white:
                    # node has not yet been explored, thus this is best path known
                    self.colour[node] = self.grey
                    heapq.heappush(self.pq, (t2, node))
                    self.dist[node] = t2

                elif self.colour[node] == self.grey and self.dist[node] > t2:
                    # if 's' -> 'u' -> 'node' is better than previously known path then update priority
                    heapq.heappush(self.pq, (t2, node))
                    self.dist[node] = t2

            # At this point the fastest path from 's' to 'u' has been found
            # so we mark 'u' as fully explored and record the dist('s', 'u')
            self.colour[u] = self.black
            self.dist[u] = t1
        return self.dist[self.end_node]

    @staticmethod
    def run_file(file) -> list:
        """
        The .data files are pickled lists in the format
        [
            [
                [...],
                [...],
                ...
            ],
            ...
        ]
        i.e. a list of adjacency lists generates by misc/dijkstra_input_parser.py
        """
        import pickle
        answers: List[Dijkstra.Distance] = []
        with open(file, 'rb') as infile:
            adjacency_lists: List[List[List[Tuple[Dijkstra.Distance, int]]]] = pickle.load(infile)
        import time
        t = time.time()
        for adj in adjacency_lists:
            d = Dijkstra(adj_list=adj)
            answers.append(d.start())
        print(time.time() - t)
        return answers


# if __name__ == '__main__':
#     Dijkstra.run_file('tests/dijkstra_input/adj_list.data')
