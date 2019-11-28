import unittest
from typing import Tuple, List, Dict, Any
from heap import Heap
import random


class TestSorting(unittest.TestCase):

    def test_simple_list(self):
        heap_instance = Heap()
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        retrieved_list = TestSorting.insert_and_extract(heap_instance, list_to_test)
        self.assertEqual(list_to_test, retrieved_list)

    def test_simple_reversed_list(self):
        heap_instance = Heap()
        list_to_test = [(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)]
        retrieved_list = TestSorting.insert_and_extract(heap_instance, list_to_test)
        self.assertEqual(list_to_test[::-1], retrieved_list)

    def test_initialised_list(self):
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        heap_instance = Heap(list_to_test[:])
        retrieved_list = []
        while heap_instance.size > 0:
            retrieved_list.append(heap_instance.pop())
        self.assertEqual(list_to_test, retrieved_list)

    def test_random_list(self):
        random.seed(16484489)
        for x in range(10):
            heap_instance = Heap()
            list_to_test = sorted([(x, x) for x in random.sample(range(1, 10 ** 9), 10 ** 3)])
            retrieved_list = TestSorting.insert_and_extract(heap_instance, list_to_test)
            self.assertEqual(list_to_test, retrieved_list)

    @staticmethod
    def insert_and_extract(heap_instance: Heap, list_to_insert: List[Tuple[Any, Any]]) -> List[Tuple[Any, Any]]:
        for number_tuple in list_to_insert:
            heap_instance.push(number_tuple[0], number_tuple[1])
        retrieved_list: List[Tuple[Any, Any]] = []
        while heap_instance.size > 0:
            retrieved_list.append(heap_instance.pop())
        return retrieved_list


if __name__ == '__main__':
    unittest.main()
