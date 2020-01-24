import random
import unittest
from typing import Tuple, List, Any

from heaps import HeapQueue


def get_random_list() -> List[Tuple[Any, Any]]:
    return [(x, x) for x in random.sample(range(1, 10 ** 9), random.randrange(10 ** 2, 10 ** 3))]


def insert_and_extract(heap_instance: HeapQueue, list_to_insert: List[Tuple[Any, Any]],
                       test_object: unittest.TestCase) -> List[Tuple[Any, Any]]:
    for number_tuple in list_to_insert:
        heap_instance.push(number_tuple[0], number_tuple[1])
    check_heap(heap_instance, test_object)
    return retrieve(heap_instance)


def retrieve(heap_instance: HeapQueue) -> List[Tuple[Any, Any]]:
    retrieved_list: List[Tuple[Any, Any]] = []
    while heap_instance.size > 0:
        retrieved_list.append(heap_instance.pop())
    return retrieved_list


def check_heap(heap_instance: HeapQueue, test_object: unittest.TestCase):
    size = len(heap_instance._array)
    for i in range(size // 2):
        if 2 * i + 1 < size:
            test_object.assertLessEqual(heap_instance._array[i], heap_instance._array[2 * i + 1])
        if 2 * i + 2 < size:
            test_object.assertLessEqual(heap_instance._array[i], heap_instance._array[2 * i + 2])


def check_heap_no_assert(heap_array: List):
    size = len(heap_array)
    for i in range(size // 2):
        if 2 * i + 1 < size:
            if not heap_array[i] <= heap_array[2 * i + 1]:
                return False
        if 2 * i + 2 < size:
            if not heap_array[i] <= heap_array[2 * i + 2]:
                return False
    return True
