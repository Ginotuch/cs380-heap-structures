from abc import abstractmethod
from typing import Tuple, Any

from .heapqueue import HeapQueue
from . import heapq2


class HeapWrapper:
    def __init__(self, **kwargs):
        self.name: str = kwargs.get("name", "")

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def push(self, priority, value) -> None:
        pass

    @abstractmethod
    def peek(self) -> Tuple[Any, Any]:
        pass


class HeapqWrapped(HeapWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.heap: list = []

    def size(self) -> int:
        return len(self.heap)

    def push(self, priority, value) -> None:
        heapq2.heappush(self.heap, (priority, value))

    def peek(self) -> Tuple[Any, Any]:
        return self.heap[0]


class HeapQueueWrapped(HeapWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.heap: HeapQueue = HeapQueue(duplicates=kwargs.get("duplicates", False))

    def size(self) -> int:
        return self.heap.size

    def push(self, priority, value) -> None:
        self.heap.push(priority, value)

    def peek(self) -> Tuple[Any, Any]:
        return self.heap.peek()
