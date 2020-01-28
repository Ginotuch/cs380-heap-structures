from abc import ABC, abstractmethod
from typing import Tuple, Any, List

from .heapqueue import HeapQueue
from . import heapq2


class HeapWrapper(ABC):
    def __init__(self, **kwargs):
        self.name: str = kwargs.get("name", "")

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def push(self, priority, key) -> None:
        pass

    @abstractmethod
    def peek(self) -> Tuple[Any, Any]:
        pass

    @abstractmethod
    def pop(self) -> Tuple[Any, Any]:
        pass

    @abstractmethod
    def get_array(self) -> List:
        pass


class HeapqWrapped(HeapWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.heap: list = kwargs.get("data", list())
        if self.size() > 0:
            heapq2.heapify(self.heap)

    def size(self) -> int:
        return len(self.heap)

    def push(self, priority, key) -> None:
        heapq2.heappush(self.heap, (priority, key))

    def peek(self) -> Tuple[Any, Any]:
        return self.heap[0]

    def pop(self) -> Tuple[Any, Any]:
        return heapq2.heappop(self.heap)

    def get_array(self) -> List:
        return self.heap


class HeapQueueWrapped(HeapWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.heap: HeapQueue = HeapQueue(duplicates=kwargs.get("duplicates", False),
                                         data=kwargs.get("data", None))

    def size(self) -> int:
        return self.heap.size

    def push(self, priority, key) -> None:
        self.heap.push(priority, key)

    def peek(self) -> Tuple[Any, Any]:
        return self.heap.peek()

    def pop(self) -> Tuple[Any, Any]:
        return self.heap.pop()

    def get_array(self) -> List:
        return self.heap._array
