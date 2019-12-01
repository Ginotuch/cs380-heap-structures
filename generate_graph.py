import random
from typing import List


class RandomConnectedGraph:
    def __init__(self, town_count=None):
        self.town_count = town_count
        if town_count is None:
            self.town_count = random.randrange(10 ** 3, 10 ** 4)
        self.adj_list: List[List] = [list() for _ in range(self.town_count)]

    def gen_graph(self):
        for town_i in range(1, self.town_count):
            num_edges = random.randrange(1, 5)
            if town_i - int(town_i * 0.75) < num_edges:
                num_edges = 1
            connect_to = random.sample(range(int(town_i * 0.75), town_i), num_edges)
            for dest_town_i in connect_to:
                self.make_edge(town_i, dest_town_i)

    def make_edge(self, town1, town2):
        self.adj_list[town1].append(town2)
        self.adj_list[town2].append(town1)


if __name__ == '__main__':
    a = RandomConnectedGraph()
    a.gen_graph()
    print()
