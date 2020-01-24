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
    def push(self, priority, value) -> None:
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

    @abstractmethod
    def heapify_up_loops(self) -> int:
        pass

    @abstractmethod
    def heapify_down_loops(self) -> int:
        pass

    @abstractmethod
    def swaps(self) -> int:
        pass

    @abstractmethod
    def reset_heapify_up_loops(self) -> int:
        pass

    @abstractmethod
    def reset_heapify_down_loops(self) -> int:
        pass

    @abstractmethod
    def reset_swaps(self) -> int:
        pass


class HeapqWrapped(HeapWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.heap: list = kwargs.get("data", list())
        if self.size() > 0:
            heapq2.heapify(self.heap)

    def size(self) -> int:
        return len(self.heap)

    def push(self, priority, value) -> None:
        heapq2.heappush(self.heap, (priority, value))

    def peek(self) -> Tuple[Any, Any]:
        return self.heap[0]

    def pop(self) -> Tuple[Any, Any]:
        return heapq2.heappop(self.heap)

    def get_array(self) -> List:
        return self.heap

    def heapify_up_loops(self) -> int:
        return heapq2.siftdown_loops

    def heapify_down_loops(self) -> int:
        return heapq2.siftup_loops

    def swaps(self) -> int:
        return heapq2.swaps

    def reset_heapify_up_loops(self) -> None:
        heapq2.siftdown_loops = 0

    def reset_heapify_down_loops(self) -> None:
        heapq2.siftup_loops = 0

    def reset_swaps(self) -> None:
        heapq2.swaps = 0


class HeapQueueWrapped(HeapWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.heap: HeapQueue = HeapQueue(duplicates=kwargs.get("duplicates", False),
                                         data=kwargs.get("data", None))

    def size(self) -> int:
        return self.heap.size

    def push(self, priority, value) -> None:
        self.heap.push(priority, value)

    def peek(self) -> Tuple[Any, Any]:
        return self.heap.peek()

    def pop(self) -> Tuple[Any, Any]:
        return self.heap.pop()

    def get_array(self) -> List:
        return self.heap._array

    def heapify_up_loops(self) -> int:
        return self.heap.heapify_up_loops

    def heapify_down_loops(self) -> int:
        return self.heap.heapify_down_loops

    def swaps(self) -> int:
        return self.heap.swaps

    def reset_heapify_up_loops(self) -> None:
        self.heap.heapify_up_loops = 0

    def reset_heapify_down_loops(self) -> None:
        self.heap.heapify_down_loops = 0

    def reset_swaps(self) -> None:
        self.heap.swaps = 0
