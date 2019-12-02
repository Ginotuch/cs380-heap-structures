"""
This will read in coordinate pairs and generate
the resulting adjacency list, then output as a
pickled list file
"""
import math
import pickle


def write_adj_lists(file):
    adj_lists = []
    with open(file) as f:
        lines = f.readlines()
        for sline in lines:
            sline = sline.strip().split(",")
            coords = [(float(sline[x]), float(sline[x + 1])) for x in range(1, len(sline) - 1, 2)]
            adj_list = [list() for _ in range(len(coords))]
            for x in range(len(coords) - 1):
                for y in range(x + 1, len(coords)):
                    node_x = coords[x]
                    node_y = coords[y]
                    dist = e_dist(node_x, node_y)
                    adj_list[x].append((y, dist))
                    adj_list[y].append((x, dist))
            adj_lists.append(adj_list)
    with open("adj_list.data", 'wb') as f:
        pickle.dump(adj_lists, f)


def e_dist(n1, n2):
    a = (n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2
    if a <= 10000.0:
        return math.sqrt(a)
    else:
        return math.inf


if __name__ == '__main__':
    write_adj_lists('tests/dijkstra_input/1.txt')
