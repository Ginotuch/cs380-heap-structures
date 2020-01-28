import unittest
import random

import tests.util as util
from heaps import HeapQueue


class TestHeapQueue(unittest.TestCase):
    _seed = random.randrange(10 ** 4, 10 ** 9)

    def test_push_random(self):
        random.seed(self._seed)
        list_to_test = util.get_random_list()
        random_items_to_push = util.get_random_list()
        heap_instance = HeapQueue(list_to_test[:])

        for loop in range(random.randrange(len(random_items_to_push) // 4, len(random_items_to_push))):
            random_item = random_items_to_push.pop(random.randrange(len(random_items_to_push)))
            heap_instance.push(random_item[0], random_item[1])
            with self.subTest(msg="push loop: " + str(loop)):
                util.check_heap(heap_instance, self)

    def test_remove_random(self):
        random.seed(self._seed)
        list_to_test = util.get_random_list()
        heap_instance = HeapQueue(list_to_test[:])

        for loop in range(random.randrange(len(list_to_test) // 2, len(list_to_test))):
            random_item = list_to_test.pop(random.randrange(len(list_to_test)))
            heap_instance.remove(random_item[1])
            with self.subTest(msg="remove loop: " + str(loop)):
                util.check_heap(heap_instance, self)

    def test_pop_random(self):
        random.seed(self._seed)
        list_to_test = sorted(util.get_random_list())
        heap_instance = HeapQueue(list_to_test[:])

        for loop, element in enumerate(list_to_test):
            with self.subTest(msg="pop loop {} element: {}".format(str(loop), str(element))):
                self.assertEqual(heap_instance.pop(), element)
                util.check_heap(heap_instance, self)

    def test_peek_random(self):
        random.seed(self._seed)
        list_to_test = sorted(util.get_random_list())
        heap_instance = HeapQueue(list_to_test[:])

        for loop, element in enumerate(list_to_test):
            with self.subTest(msg="peek loop {} element: {}".format(str(loop), str(element))):
                self.assertEqual(heap_instance.peek(), element)
                heap_instance.pop()
                util.check_heap(heap_instance, self)

    def test_get_priority_random(self):
        random.seed(self._seed)
        element_count = random.randrange(10 ** 2, 10 ** 3)
        list_keys = random.sample(range(1, 10 ** 9), element_count)
        list_priorities = random.sample(range(1, 10 ** 9), element_count)
        list_to_test = [(list_priorities[i], list_keys[i]) for i in range(element_count)]
        heap_instance = HeapQueue(list_to_test[:])

        for loop, element in enumerate(list_to_test):
            with self.subTest(msg="get_priority loop {} element {}".format(str(loop), str(element))):
                self.assertEqual(heap_instance.get_priority(element[1]), element[0])

    def test_exists_random(self):
        random.seed(self._seed)
        list_to_test = util.get_random_list()
        heap_instance = HeapQueue(list_to_test[:])
        self.assertFalse(heap_instance.exists("Test"))
        self.assertFalse(heap_instance.exists(-1))

        for element in list_to_test:
            with self.subTest(msg="exists element: " + str(element)):
                self.assertTrue(heap_instance.exists(element[1]))
            with self.subTest(msg="not exists element: " + str(element)):
                self.assertFalse(heap_instance.exists(random.choice(list_to_test)[1] + 0.5))

    def test_extend_random(self):
        random.seed(self._seed)
        list_to_test = util.get_random_list()
        list_to_extend = [(x[0] + 0.5, x[1] + 0.5) for x in list_to_test[len(list_to_test) // 2:]]
        full_list = sorted(list_to_test + list_to_extend)
        heap_instance = HeapQueue(list_to_test[:])
        heap_instance.extend(list_to_extend)
        self.assertEqual(heap_instance.size, len(heap_instance._array))
        util.check_heap(heap_instance, self)
        retrieved_list = util.retrieve(heap_instance)
        self.assertEqual(full_list, retrieved_list)

    def test_extend_empty_random(self):
        random.seed(self._seed)
        list_to_test = util.get_random_list()
        heap_instance = HeapQueue()
        heap_instance.extend(list_to_test[:])
        self.assertEqual(heap_instance.size, len(heap_instance._array))
        util.check_heap(heap_instance, self)
        retrieved_list = util.retrieve(heap_instance)
        self.assertEqual(sorted(list_to_test), retrieved_list)

    def test__process_data_random(self):
        random.seed(self._seed)
        list_to_test_in = util.get_random_list()
        list_to_test_check = list_to_test_in[:]
        heap_instance = HeapQueue()
        heap_instance._process_data(list_to_test_in)
        self.assertEqual(sorted(list_to_test_in), sorted(list_to_test_check), msg="Input should not change")

        list_to_test_check = util.get_random_list()
        list_to_test_in = [x[0] for x in list_to_test_check]
        heap_instance = HeapQueue(priorities=False)
        heap_instance._process_data(list_to_test_in)
        self.assertEqual(sorted(list_to_test_in), sorted(list_to_test_check), msg="Input data not converted to tuples")

    def test__heapify_random(self):
        random.seed(self._seed)
        list_to_test = util.get_random_list()
        heap_instance = HeapQueue()
        heap_instance._array = list_to_test[:]
        heap_instance.size = len(list_to_test)
        heap_instance._heapify()
        util.check_heap(heap_instance, self)

    def test__delete_random(self):
        random.seed(self._seed)
        list_to_test = util.get_random_list()
        heap_instance = HeapQueue(list_to_test[:])
        heap_instance._delete(0)
        util.check_heap(heap_instance, self)
        heap_instance._delete(heap_instance.size - 1)
        util.check_heap(heap_instance, self)
        heap_instance._delete(heap_instance.size // 2)
        util.check_heap(heap_instance, self)

        self.assertEqual(heap_instance.size, len(heap_instance._array))

        for loop in range(random.randrange(heap_instance.size)):
            random_index_to_delete = random.randrange(heap_instance.size)
            with self.subTest(msg="seed {} loop {} deleted index {}".format(self._seed, loop, random_index_to_delete)):
                heap_instance._delete(random_index_to_delete)
                util.check_heap(heap_instance, self)

    def test__heapify_down_random(self):
        random.seed(self._seed)
        list_to_test = util.get_random_list()
        heap_instance = HeapQueue(list_to_test[:])
        new_big_element = max(list_to_test)
        new_big_element = (new_big_element[0] + random.randrange(20), new_big_element[1] + random.randrange(20))
        heap_instance._array = [new_big_element] + heap_instance._array[1:]
        heap_instance._heapify_down(0)
        util.check_heap(heap_instance, self)

    def test__heapify_up_random(self):
        random.seed(self._seed)
        list_to_test = util.get_random_list()
        heap_instance = HeapQueue(list_to_test[:])
        heap_instance.size += 1
        heap_instance._array = heap_instance._array + [(0, 0)]
        heap_instance._heapify_up(heap_instance.size - 1)
        util.check_heap(heap_instance, self)

    def test__swap_random(self):
        random.seed(self._seed)
        list_to_test = util.get_random_list()
        heap_instance = HeapQueue(list_to_test[:])
        self.assertFalse(heap_instance._swap(1, 3))
        self.assertFalse(heap_instance._swap(0, 1))
        temp_element = heap_instance._array[1]
        heap_instance._array[1] = heap_instance._array[0]
        heap_instance._array[0] = (temp_element[0] + 1, temp_element[1] + 1)
        self.assertTrue(heap_instance._swap(0, 1))
        self.assertFalse(heap_instance._swap(0, 1))
