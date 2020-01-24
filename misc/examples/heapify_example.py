"""

"""
import time

from tests.util import check_heap_no_assert
from typing import List, Tuple, Any
from misc.debug_versions.wrappers import HeapqWrapped, HeapQueueWrapped
import random


def get_random_list(p) -> List[Tuple[Any, Any]]:
    return [(x, x) for x in random.sample(range(1, 10 ** (p + 1)), 10 ** p)]


for power in range(2, 7, 1):
    print()
    print("=" * 15)
    print("Nodes: 10^{:d}".format(power))
    print("=" * 15)
    nodes1 = get_random_list(power)
    nodes2 = nodes1[:]

    heaps = ((HeapQueueWrapped, "HeapQueue duplicates", nodes1), (HeapqWrapped, "Heapq", nodes2))
    for heap_set in heaps:
        t = time.time()
        heap = heap_set[0](name=heap_set[1], duplicates=True, data=heap_set[2])
        end = time.time() - t
        print("Stats of", heap.name)
        print(" heap correct?", check_heap_no_assert(heap.get_array()))
        print(" heapifydown loops:", heap.heapify_down_loops())
        print(" heapifyup loops:", heap.heapify_up_loops())
        print(" swaps:", heap.swaps())
        heap.reset_heapify_down_loops()  # resets number of loops before pop
        heap.reset_heapify_up_loops()
        heap.reset_swaps()
        print(" time:", end)
        print()
