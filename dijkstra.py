import math
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

            for node, cost in self.adjacency_list[u]:
                t2 = t1 + cost
                if self.colour[node] == self.white:
                    self.colour[node] = self.grey
                    self.pq.push(t2, node)
                elif self.colour[node] == self.grey and self.pq.get_key(node) > t2:
                    self.pq.push(t2, node)
            self.colour[u] = self.black
            self.dist[u] = t1
        return self.dist[self.end_node]

    @staticmethod
    def run_file(file):
        answers = []
        with open(file) as f:
            lines = f.readlines()

            for sline in lines:
                sline = sline.strip().split(",")
                coords = [(float(sline[x]), float(sline[x + 1])) for x in range(1, len(sline) - 1, 2)]
                start = coords[0]
                end = coords[-1]
                adj_list = [list() for _ in range(len(coords))]
                for x in range(len(coords) - 1):
                    for y in range(x + 1, len(coords)):

                        node_x = coords[x]
                        node_y = coords[y]
                        dist = Dijkstra.e_dist(node_x, node_y)
                        adj_list[x].append((y, dist))
                        adj_list[y].append((x, dist))
                d = Dijkstra(adj_list=adj_list)
                length = d.start()
                if length == inf:
                    answer = -1
                else:
                    answer = "{:.2f}".format(length)
                answers.append(answer)

    @staticmethod
    def e_dist(n1, n2):
        a = (n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2
        if a <= 10000.0:
            return math.sqrt(a)
        else:
            return inf


if __name__ == '__main__':
    Dijkstra.run_file("tests/dijkstra_input/a4q2in3.txt")
