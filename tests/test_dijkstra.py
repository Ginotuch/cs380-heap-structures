import math
import unittest
import pickle
from dijkstra import Dijkstra
import os


class TestDijkstra(unittest.TestCase):
    def test_in_outs(self):
        inputs = "dijkstra_input"
        outputs = "dijkstra_output"
        answer_pairs = [
            ('adj_list.data', '1.txt'),
            ('adj_list2.data', '2.txt'),
            ('adj_list3.data', '3.txt')
        ]

        for pair in answer_pairs:
            with open(os.path.join(inputs, pair[0]), 'rb') as file_list:
                test_adj_lists = pickle.load(file_list)
            with open(os.path.join(outputs, pair[1])) as answer_list:
                answer_string = [x.strip() for x in answer_list.readlines()]
            distance_returns = []
            for adj_list in test_adj_lists:
                d = Dijkstra(adj_list=adj_list)
                dist_temp = d.start()
                if dist_temp == math.inf:
                    dist_temp = str(-1)
                else:
                    dist_temp = "{:.2f}".format(dist_temp)
                distance_returns.append(dist_temp)
            self.assertEqual(distance_returns, answer_string, "Failed on:" + str(pair))


if __name__ == '__main__':
    unittest.main()
