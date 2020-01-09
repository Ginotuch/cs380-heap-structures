from typing import Tuple, List, Dict, Any


class Heap:
    def __init__(self, data: List[Tuple] = None, allow_duplicates: bool = False, priorities: bool = True):
        self._array: List[Tuple[Any, Any]] = []
        self._positions: Dict[Any, int] = {}
        self._duplicates: bool = allow_duplicates
        self._priorities: bool = priorities
        self.size: int = 0
        if data is not None:
            self._heapify(data)

    def push(self, key, value=None) -> None:  # will also update priority if already in the heap
        if not self._priorities:
            if value is not None:
                raise Exception("Priorities are disabled yet both a key and value were supplied")
            value = key
        if not self._duplicates and value in self._positions:  # updates priority if value already in heap
            position = self._positions[value]
            if key > self._array[position][0]:
                self._array[position] = (key, self._array[position][1])
                self._heapify_down(position)
            elif key < self._array[position][0]:
                self._array[position] = (key, self._array[position][1])
                self._heapify_up(position)
        else:  # otherwise add the new element
            if not self._duplicates:
                self._positions[value] = self.size
            self._array.append((key, value))
            self.size += 1
            self._heapify_up(self.size - 1)

    def remove(self, value) -> Tuple[Any, Any]:
        try:
            position: int = self._positions[value]
        except KeyError:
            raise KeyError("Value not in heap")
        else:
            return self._delete(position)

    def pop(self) -> Tuple[Any, Any]:
        return self._delete(0)

    def peek(self) -> Tuple[Any, Any]:
        return self._array[0]

    def get_key(self, value) -> Any:
        return self._array[self._positions[value]][0]

    def _heapify(self, data: List[Tuple]) -> None:  # in-place-ish ingest
        self._array = data
        self.size = len(self._array)

        for i in range(self.size):  # checks that elements are in correct format of (key, value)
            if not self._priorities:
                self._array[i] = (self._array[i], self._array[i])
            elif len(self._array[i]) != 2:
                raise Exception("Elements must be in format: (key, value) where key is a comparable priority")
            if not self._duplicates:
                if self._array[i][1] in self._positions:  # should it automatically remove duplicates? (if so how)
                    raise Exception("Duplicates disabled yet duplicate elements exist in input data")
                else:
                    self._positions[self._array[i][1]] = i

        for i in reversed(range(self.size // 2)):  # in-place heapify
            self._heapify_down(i)

    def _delete(self, i: int) -> Tuple[Any, Any]:
        deleted: Tuple[Any, Any] = self._array[i]
        old_leaf: Tuple[Any, Any] = self._array[-1]
        self._array[i] = old_leaf
        if not self._duplicates:
            self._positions[self._array[i][1]] = i  # update position of swapped element
            self._positions.pop(deleted[1])
        self._array.pop()

        self.size -= 1
        if deleted > old_leaf and i < self.size:
            self._heapify_up(i)
        else:
            self._heapify_down(i)
        return deleted

    def _heapify_down(self, i: int) -> None:
        while 2 * i + 1 < self.size:
            left_child_i = 2 * i + 1
            right_child_i = 2 * i + 2
            big_child_i = left_child_i
            if right_child_i < self.size and self._array[left_child_i] >= self._array[right_child_i]:
                big_child_i = right_child_i
            if not self._swap(i, big_child_i):
                break
            i = big_child_i

    def _heapify_up(self, i: int) -> None:
        while i > 0:
            parent_index: int = (i - 1) >> 1
            if not self._swap(parent_index, i):
                break
            i = parent_index

    def _swap(self, parent_index: int, child_index: int) -> bool:  # If no swap happens then heapify is complete
        parent: Tuple[Any, Any] = self._array[parent_index]
        child: Tuple[Any, Any] = self._array[child_index]

        if parent > child:
            if not self._duplicates:
                self._positions[parent[1]] = child_index
                self._positions[child[1]] = parent_index
            self._array[parent_index] = child
            self._array[child_index] = parent
            return True
        else:
            return False

    def _check_heap(self):
        for i in range(self.size // 2):
            if 2 * i + 1 < self.size:
                assert self._array[i] <= self._array[2 * i + 1]
            if 2 * i + 2 < self.size:
                assert self._array[i] <= self._array[2 * i + 2]


if __name__ == "__main__":
    h = Heap([(6, 54), (3, 23)])
    h.push(5, 67)
    h.push(4, 88)
    h.push(6, 55)
    h.push(1, 20)
    h.pop()
    print()
    print()