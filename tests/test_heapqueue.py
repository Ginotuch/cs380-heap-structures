import unittest

import tests.util as util
from heaps import HeapQueue


class TestHeapQueue(unittest.TestCase):
    def test_push(self):
        list_to_test = [(1, 1), (3, 3), (5, 5), (6, 6), (8, 8)]
        heap_instance = HeapQueue(list_to_test[:])
        heap_instance.push(7, 7)
        util.check_heap(heap_instance, self)
        heap_instance.push(2, 2)
        util.check_heap(heap_instance, self)
        heap_instance.push(4, 4)
        util.check_heap(heap_instance, self)

    def test_remove(self):
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        heap_instance = HeapQueue(list_to_test[:])
        self.assertEqual(heap_instance.remove(2), (2, 2))
        util.check_heap(heap_instance, self)
        self.assertEqual(heap_instance.remove(3), (3, 3))
        util.check_heap(heap_instance, self)

    def test_pop(self):
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        heap_instance = HeapQueue(list_to_test[:])
        for element in list_to_test:
            with self.subTest(msg="pop element: " + str(element)):
                self.assertEqual(heap_instance.pop(), element)
                util.check_heap(heap_instance, self)

    def test_peek(self):
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        heap_instance = HeapQueue(list_to_test[:])
        self.assertEqual(heap_instance.peek(), (1, 1))
        heap_instance.pop()
        self.assertEqual(heap_instance.peek(), (2, 2))

    def test_get_priority(self):
        test_tuple_element = (99, 4567)
        list_to_test = [(1, "test1"), (2, 56), (3, 3), (4, 4), (5, 5), (20, test_tuple_element)]
        heap_instance = HeapQueue(list_to_test[:])
        self.assertEqual(heap_instance.get_priority("test1"), 1)
        self.assertEqual(heap_instance.get_priority(56), 2)
        self.assertEqual(heap_instance.get_priority(4), 4)
        self.assertEqual(heap_instance.get_priority(test_tuple_element), 20)

    def test_exists(self):
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        heap_instance = HeapQueue(list_to_test[:])
        for element in list_to_test:
            with self.subTest(msg="exists element: " + str(element)):
                self.assertTrue(heap_instance.exists(element[1]))

    def test__heapify(self):
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        heap_instance = HeapQueue()
        heap_instance._heapify(list_to_test[:])
        util.check_heap(heap_instance, self)

    def test__delete(self):
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        heap_instance = HeapQueue(list_to_test[:])
        heap_instance._delete(0)
        util.check_heap(heap_instance, self)
        heap_instance._delete(heap_instance.size - 1)
        util.check_heap(heap_instance, self)
        heap_instance._delete(heap_instance.size // 2)
        util.check_heap(heap_instance, self)

    def test__heapify_down(self):
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        heap_instance = HeapQueue(list_to_test[:])
        heap_instance.size += 1
        heap_instance._array = [(99, 99)] + heap_instance._array
        heap_instance._heapify_down(0)
        util.check_heap(heap_instance, self)

    def test__heapify_up(self):
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        heap_instance = HeapQueue(list_to_test[:])
        heap_instance.size += 1
        heap_instance._array = heap_instance._array + [(0, 0)]
        heap_instance._heapify_up(heap_instance.size - 1)
        util.check_heap(heap_instance, self)

    def test__swap(self):
        list_to_test = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        heap_instance = HeapQueue(list_to_test[:])
        self.assertFalse(heap_instance._swap(1, 3))
        self.assertFalse(heap_instance._swap(0, 1))
        temp_element = heap_instance._array[1]
        heap_instance._array[1] = heap_instance._array[0]
        heap_instance._array[0] = temp_element
        self.assertTrue(heap_instance._swap(0, 1))
        self.assertFalse(heap_instance._swap(0, 1))
