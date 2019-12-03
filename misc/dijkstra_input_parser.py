"""
This will read in coordinate pairs and generate
the resulting adjacency list, then output as a
pickled list file
"""
import math
import pickle
from typing import List, Tuple


def write_adj_lists(file):
    adj_lists = []
    with open(file) as f:
        lines: List[str] = f.readlines()
        for sline in lines:
            coord_list: list = sline.strip().split(",")
            coords: List[Tuple[float, float]] = [(float(coord_list[x]), float(coord_list[x + 1])) for x in
                                                 range(1, len(coord_list) - 1, 2)]
            adj_list: List[List[Tuple[float, float]]] = [list() for _ in range(len(coords))]
            for x in range(len(coords) - 1):
                for y in range(x + 1, len(coords)):
                    node_x: Tuple[float, float] = coords[x]
                    node_y: Tuple[float, float] = coords[y]
                    dist: float = e_dist(node_x, node_y)
                    if dist != math.inf:
                        adj_list[x].append((y, dist))
                        adj_list[y].append((x, dist))
            adj_lists.append(adj_list)
    with open("adj_list.data", 'wb') as f:
        pickle.dump(adj_lists, f)


def e_dist(n1: Tuple[float, float], n2: Tuple[float, float]):
    a = (n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2
    if a <= 10000.0:
        return math.sqrt(a)
    else:
        return math.inf


if __name__ == '__main__':
    write_adj_lists('tests/dijkstra_input/1.txt')
