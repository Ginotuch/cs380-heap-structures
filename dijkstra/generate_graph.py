import random
from typing import List, Tuple


class RandomConnectedGraph:
    def __init__(self, town_count: int = None):
        self.town_count: int = town_count
        if town_count is None:
            self.town_count = random.randrange(10 ** 3, 10 ** 4)
        self.adj_list: List[List[Tuple]] = [list() for _ in range(self.town_count)]

    def gen_graph(self) -> None:
        for town_i in range(1, self.town_count):
            sub_towns: int = int(town_i * (random.randrange(75, 100) / 100))
            num_edges: int = random.randrange(1, 5)
            if town_i - sub_towns < num_edges:
                num_edges = 1
            connect_to: List[int] = random.sample(range(sub_towns, town_i), num_edges)
            for dest_town_i in connect_to:
                self.make_edge(town_i, dest_town_i, random.randrange(100))

    def get_bad_graph(self) -> None:
        """Creates a graph that slows down heapq implementation of Dijkstra"""
        cost: int = self.town_count * 2
        for town_i in range(0, self.town_count - 1):
            self.make_edge(town_i, town_i + 1, 0)
            self.make_edge(town_i, self.town_count - 1, cost)
            cost = cost - 1
        self.make_edge(self.town_count - 2, self.town_count - 1, cost)

    def make_edge(self, town1, town2, cost) -> None:
        self.adj_list[town1].append((town2, cost))
        self.adj_list[town2].append((town1, cost))


if __name__ == '__main__':
    a = RandomConnectedGraph()
    a.gen_graph()
    print()
