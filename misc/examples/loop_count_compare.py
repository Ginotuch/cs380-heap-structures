"""
Shows a weird case of heapq requiring logn operations for
heapifydown (siftup in heapq) even though it's not required.
"""
import time
from typing import List
from misc.debug_versions.wrappers import HeapWrapper, HeapqWrapped, HeapQueueWrapped

for power in range(2, 21, 2):
    print()
    print("=" * 15)
    print("Updates: 2^{:d} - 2".format(power))
    print("=" * 15)

    node_count = 2 ** power - 2
    nodes = [(1, 1) for x in range(node_count)]
    heaps: List[HeapWrapper] = [
        HeapQueueWrapped(name="HeapQueue duplicates", duplicates=True, data=nodes[:]),
        HeapqWrapped(name="Heapq", data=nodes[:])
    ]
    for heap_i, heap in enumerate(heaps):
        print("Starting on", heap.name)
        print(" heapifydown loops:", heap.heapify_down_loops())
        print(" heapifyup loops:", heap.heapify_up_loops())
        print(" swaps:", heap.swaps())
        heap.reset_heapify_down_loops()  # resets number of loops before pop
        heap.reset_heapify_up_loops()
        heap.reset_swaps()
        print(" Reset stats and starting pop:")
        t = time.time()
        heap.pop()
        print("  Time taken:", time.time() - t)
        print("  heapifydown loops:", heap.heapify_down_loops())
        print("  heapifyup loops:", heap.heapify_up_loops())
        print("  swaps:", heap.swaps())
        print()
