import unittest
from heap import Heap
import random


class TestSorting(unittest.TestCase):

    def test_simple_list(self):
        heap_instance = Heap()
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        for number_tuple in list_to_test:
            heap_instance.push(number_tuple[0], number_tuple[1])
        retrieved_list = []
        while heap_instance.size > 0:
            retrieved_list.append(heap_instance.pop())
        self.assertEqual(list_to_test, retrieved_list)

    def test_simple_reversed_list(self):
        heap_instance = Heap()
        list_to_test = [(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)]
        for number_tuple in list_to_test:
            heap_instance.push(number_tuple[0], number_tuple[1])
        retrieved_list = []
        while heap_instance.size > 0:
            retrieved_list.append(heap_instance.pop())
        self.assertEqual(list_to_test[::-1], retrieved_list)

    def test_initialised_list(self):
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        list_to_compare = [x[0] for x in list_to_test]
        heap_instance = Heap(list_to_test)
        retrieved_list = []
        while heap_instance.size > 0:
            retrieved_list.append(heap_instance.pop()[0])
        self.assertEqual(list_to_compare, retrieved_list)

    def test_random_list(self):
        heap_instance = Heap()
        random.seed(16484489)
        for x in range(10):
            list_to_test = sorted([(x, x) for x in random.sample(range(1, 10 ** 9), 10 ** 3)])
            for number_tuple in list_to_test:
                heap_instance.push(number_tuple[0], number_tuple[1])
            retrieved_list = []
            while heap_instance.size > 0:
                retrieved_list.append(heap_instance.pop())
            self.assertEqual(list_to_test, retrieved_list)


if __name__ == '__main__':
    unittest.main()
