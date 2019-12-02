from math import inf

from heap import Heap
from generate_graph import RandomConnectedGraph


class Dijkstra:
    def __init__(self, node_count=100000, adj_list=None):
        self.adjacency_list = adj_list
        if adj_list is None:
            self.graph = RandomConnectedGraph(node_count)
            self.graph.gen_graph()
            self.adjacency_list = self.graph.adj_list
        self.pq = Heap()
        self.colour = [0] * len(self.adjacency_list)
        self.dist = [inf] * len(self.adjacency_list)
        self.white = 0  # Unexplored nodes
        self.grey = 1  # Partially explored nodes (shortest path not yet known)
        self.black = 2  # Fully explored nodes (shortest path known)
        self.end_node = len(self.adjacency_list) - 1

    def start(self):
        self.pq.push(0, 0)  # Pushing source node 's' to queue. Distance to itself is 0
        while self.pq.size > 0:
            t1, u = self.pq.pop()  # 't1' = cost from 's' to 'u'

            if self.colour[u] == self.black:
                raise Exception("Something went wrong")

            if u == self.end_node:  # If 'u' is the desired node, then we have already found the shortest path
                self.dist[u] = t1
                break

            for node, cost in self.adjacency_list[u]:

                # 'cost' is dist('u', 'node')
                # 't2' is dist('s', 'u') + dist('u', 'node'). (path to 'node' through 'u')
                t2 = t1 + cost

                if self.colour[node] == self.white:
                    # node has not yet been explored, thus this is best path known
                    self.colour[node] = self.grey
                    self.pq.push(t2, node)

                elif self.colour[node] == self.grey and self.pq.get_key(node) > t2:
                    # if 's' -> 'u' -> 'node' is better than previously known path then update priority
                    self.pq.push(t2, node)

            # At this point the fastest path from 's' to 'u' has been found
            # so we mark 'u' as fully explored and record the dist('s', 'u')
            self.colour[u] = self.black
            self.dist[u] = t1
        return self.dist[self.end_node]

    @staticmethod
    def run_file(file):
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
        answers = []
        with open(file, 'rb') as infile:
            adjacency_lists = pickle.load(infile)
        for adj in adjacency_lists:
            d = Dijkstra(adj_list=adj)
            answers.append(d.start())
        return answers


if __name__ == '__main__':
    Dijkstra.run_file('tests/dijkstra_input/adj_list.data')
