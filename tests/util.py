import random
from typing import Tuple, List, Any

from heaps.heap import Heap


def get_random_list() -> List[Tuple[Any, Any]]:
    return [(x, x) for x in random.sample(range(1, 10 ** 9), random.randrange(10 ** 2, 10 ** 3))]


def insert_and_extract(heap_instance: Heap, list_to_insert: List[Tuple[Any, Any]]) -> List[Tuple[Any, Any]]:
    for number_tuple in list_to_insert:
        heap_instance.push(number_tuple[0], number_tuple[1])
    heap_instance._check_heap()
    return retrieve(heap_instance)


def retrieve(heap_instance: Heap) -> List[Tuple[Any, Any]]:
    retrieved_list: List[Tuple[Any, Any]] = []
    while heap_instance.size > 0:
        retrieved_list.append(heap_instance.pop())
    return retrieved_list
