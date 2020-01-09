import random
import unittest

import tests.util as util
from heaps import HeapQueue


class TestSorting(unittest.TestCase):
    _seed = random.randrange(10 ** 4, 10 ** 9)

    def test_simple_list(self):
        heap_instance = HeapQueue()
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        retrieved_list = util.insert_and_extract(heap_instance, list_to_test, self)
        self.assertEqual(list_to_test, retrieved_list)

    def test_simple_reversed_list(self):
        heap_instance = HeapQueue()
        list_to_test = [(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)]
        retrieved_list = util.insert_and_extract(heap_instance, list_to_test, self)
        self.assertEqual(list_to_test[::-1], retrieved_list)

    def test_simple_initialised_list(self):
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        heap_instance = HeapQueue(list_to_test[:])
        retrieved_list = util.retrieve(heap_instance)
        self.assertEqual(list_to_test, retrieved_list)

    def test_random_list(self):
        random.seed(self._seed)
        for x in range(20):
            heap_instance = HeapQueue()
            list_to_test = util.get_random_list()
            retrieved_list = util.insert_and_extract(heap_instance, list_to_test, self)
            with self.subTest(msg="Loop: " + str(x)):
                self.assertEqual(sorted(list_to_test), retrieved_list, "Random seed: ({})".format(str(self._seed)))

    def test_random_list_same_instance(self):
        random.seed(self._seed)
        heap_instance = HeapQueue()
        for x in range(20):
            list_to_test = util.get_random_list()
            retrieved_list = util.insert_and_extract(heap_instance, list_to_test, self)
            with self.subTest(msg="Loop: " + str(x)):
                self.assertEqual(sorted(list_to_test), retrieved_list, "Random seed: ({})".format(str(self._seed)))

    def test_random_deletion(self):
        random.seed(self._seed)
        for x in range(20):
            list_to_test = util.get_random_list()
            heap_instance = HeapQueue(list_to_test[:])
            util.check_heap(heap_instance, self)
            index_to_delete = random.randrange(0, len(list_to_test))
            deleted_element = list_to_test.pop(index_to_delete)
            heap_instance.remove(deleted_element[1])
            util.check_heap(heap_instance, self)
            with self.subTest(msg="peek check - loop: " + str(x)):
                self.assertEqual(heap_instance.peek(), min(list_to_test))
            retrieved_list = util.retrieve(heap_instance)
            with self.subTest(msg="sorted check - loop: " + str(x)):
                self.assertEqual(sorted(list_to_test), retrieved_list, "Random seed: ({})".format(str(self._seed)))

    def test_random_deletion_same_insatnce(self):
        """
        Will randomly delete 10 to 90 elements from a list and also from the heap
        then verify that the heap deleted these elements correctly, checking
        for sorted extraction of the elements.
        """
        random.seed(self._seed)
        for run in range(20):
            list_to_test = util.get_random_list()
            heap_instance = HeapQueue(list_to_test[:])
            util.check_heap(heap_instance, self)
            for deletion in range(random.randrange(10, 90)):
                index_to_delete = random.randrange(0, len(list_to_test))
                deleted_element = list_to_test.pop(index_to_delete)
                heap_instance.remove(deleted_element[1])
                util.check_heap(heap_instance, self)
            with self.subTest(msg="Loop: " + str(run)):
                self.assertEqual(heap_instance.peek(), min(list_to_test))
            retrieved_list = util.retrieve(heap_instance)
            with self.subTest(msg="Loop: " + str(run)):
                self.assertEqual(sorted(list_to_test), retrieved_list, "Random seed: ({})".format(str(self._seed)))
