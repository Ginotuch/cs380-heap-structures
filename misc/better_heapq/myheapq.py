"""
A faster implementation of _siftup from heapq.
Heapifying 20,000,000 elements on an Intel i5-8250U (8 cores) @ 3.4GHz:
myheapq: average of 7.7s
heapq: average of 10.5s
"""


def heappush(heap, item):
    heap.append(item)
    _siftdown(heap, len(heap) - 1)

def heappop(heap):
    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt

def heapify(x):
    for i in reversed(range(len(x)//2)):
        _siftup(x, i)

def _siftdown(heap, pos):
    while pos > 0:
        parent_index = (pos - 1) >> 1
        if heap[parent_index] > heap[pos]:
            temp = heap[parent_index]
            heap[parent_index] = heap[pos]
            heap[pos] = temp
            pos = parent_index
            continue
        break

def _siftup(heap, pos):
    n = len(heap)
    childpos = 2 * pos + 1
    while childpos < n:
        rightpos = childpos + 1
        if rightpos < n and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        if heap[pos] > heap[childpos]:
            temp = heap[pos]
            heap[pos] = heap[childpos]
            heap[childpos] = temp
            pos = childpos
            childpos = 2*pos + 1
        else:
            break