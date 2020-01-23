import os
import psutil

process = psutil.Process(os.getpid())
def mem():
    return "RAM usage: " + str(round(process.memory_info().rss * 1e-6, 2)) + "MB"