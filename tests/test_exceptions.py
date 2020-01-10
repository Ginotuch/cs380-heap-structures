import unittest
import heaps


class TestExceptions(unittest.TestCase):

    def test_UnexpectedPriority(self):
        list_to_test = [1, 2, 3, 4, 5]
        heap_instance: heaps.HeapQueue = heaps.HeapQueue(list_to_test, priorities=False)
        with self.assertRaises(heaps.UnexpectedPriority):
            heap_instance.push(6, 6)

    def test_DuplicatesEnabled(self):
        list_to_test = [(1, 1), (1, 1), (3, 3), (3, 3), (5, 5)]
        heap_instance: heaps.HeapQueue = heaps.HeapQueue(list_to_test, allow_duplicates=True)
        with self.assertRaises(heaps.DuplicatesEnabled):
            heap_instance.remove(1)
        with self.assertRaises(heaps.DuplicatesEnabled):
            heap_instance.get_key(1)

    def test_BadData_too_long(self):
        list_to_test = [(1, 1, 1), (2, 2), (3, 3, 3), (4, 4), (5, 5)]
        with self.assertRaises(heaps.BadData):
            heaps.HeapQueue(list_to_test)

    def test_BadData_not_Tuple(self):
        list_to_test = [1, (2, 2), 3, (4, 4), (5, 5)]
        with self.assertRaises(heaps.BadData):
            heaps.HeapQueue(list_to_test)

    def test_BadData_no_raise(self):
        list_to_test = [(1, 1, 1), (2, 2), (3, 3, 3, 3, 3, 3), (4, 4), (5, 5)]
        try:
            heaps.HeapQueue(list_to_test, priorities=False)
        except heaps.BadData:
            self.fail("heaps.BadData exception should no be raised")

    def test_DuplicateInputs(self):
        list_to_test = [(1, 1), (1, 1), (3, 3), (3, 3), (5, 5)]
        with self.assertRaises(heaps.DuplicateInputs):
            heaps.HeapQueue(list_to_test)
