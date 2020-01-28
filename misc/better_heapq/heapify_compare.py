"""
Runs a comparison of heapq and myheapq (the different
_siftup functions)
"""

import heapq2, myheapq, random, time
from tests.util import check_heap_no_assert
import pickle

# def get_random_list(p):
#     random.seed(4567)
#     return random.sample(range(0, 2 ** (p + 1)), 2 ** p * 2)
#
# for power in range(2, 24 + 2, 2):
#     print("starting", power)
#     with open("pik{}.data".format(str(power)), "wb") as pout:
#         pickle.dump(get_random_list(power), pout)
#     print("next\n")

for power in range(2, 24 + 2, 2):
    print("power", power)
    with open("pik{}.data".format(str(power)), "rb") as pin:
        alist = pickle.load(pin)
        t = time.time()
        myheapq.heapify(alist)
        print("myheapq", time.time() - t)
        alist[0] = 0
        alist = None
    with open("pik{}.data".format(str(power)), "rb") as pin:
        alist = pickle.load(pin)
        t = time.time()
        heapq2.heapify(alist)
        print("heapq", time.time() - t)
        alist[0] = 0
    print()
