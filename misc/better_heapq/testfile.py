"""
Runs a comparison of heapq and myheapq (the different
_siftup functions)
"""

import heapq2, myheapq, random, time
from tests.util import check_heap_no_assert
import pickle

# def get_random_list(p):
#     random.seed(4567)
#     return random.sample(range(1, 10 ** (p + 1)), 10 ** p * 2)
#
# alist = get_random_list(7)
#
# with open("pik.data", 'wb') as f:
#     pickle.dump(alist, f)

# with open("pik.data", "rb") as f:
#     alist= pickle.load(f)
#
# alist2 = alist[:]
# t = time.time()
# heapq2.heapify(alist)
# print(time.time() - t)
# print("correct:", check_heap_no_assert(alist))
print("myheapq")
for x in range(3):
    with open("pik.data", "rb") as f:
        alist = pickle.load(f)
    t = time.time()
    myheapq.heapify(alist)
    print(time.time() - t)
    print("correct:", check_heap_no_assert(alist))
alist = []
print("\nheapq")
for x in range(3):
    with open("pik.data", "rb") as f:
        alist = pickle.load(f)
    t = time.time()
    heapq2.heapify(alist)
    print(time.time() - t)
    print("correct:", check_heap_no_assert(alist))
