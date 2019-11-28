from typing import Tuple, List, Dict, Any


class Heap:
    def __init__(self, data=None):
        self._array: List[Tuple[Any, Any]] = []
        self._positions: Dict[Any, int] = {}
        self.size: int = 0
        try:
            for item in data:
                if len(item) != 2:
                    raise Exception("Items must be in format: (key, value) where key is a comparable priority")
                self.push(item[0], item[1])
        except TypeError as e:
            raise e

    def push(self, key, value) -> None:  # will also update priority if already in the heap
        if value in self._positions:
            position = self._positions[value]
            if key > self._array[position][0]:
                self._array[position] = (key, self._array[position][1])
                self._heapify_down(position)
            else:
                self._array[position] = (key, self._array[position][1])
                self._heapify_up(position)
        else:
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

    def _delete(self, i: int) -> Tuple[Any, Any]:
        deleted: Tuple[Any, Any] = self._array[i]
        self._array[i] = self._array[-1]
        self._positions[self._array[i][1]] = i  # update position of swapped element
        self._array.pop()
        self._positions.pop(deleted[1])
        self.size -= 1
        self._heapify_down(i)
        return deleted

    def _heapify_down(self, i: int) -> None:  # todo: unsure if minimising left/right child matters
        while 2 * i + 1 < self.size:
            left_child_i = 2 * i + 1
            right_child_i = 2 * i + 2
            big_child_i = left_child_i
            if right_child_i < self.size and self._array[right_child_i] < self._array[left_child_i]:
                big_child_i = right_child_i
            parent = self._array[i]
            child = self._array[big_child_i]
            if parent > child:
                self._positions[parent[1]] = big_child_i
                self._positions[child[1]] = i
                self._array[i] = child
                self._array[big_child_i] = parent
                i = big_child_i
            else:
                return

    def _heapify_up(self, i: int) -> None:
        while i > 0 and (parent := self._array[(parent_i := (i - 1) >> 1)]) > (child := self._array[i]):
            self._positions[parent[1]] = i
            self._positions[child[1]] = parent_i
            self._array[parent_i] = child
            self._array[i] = parent

            i = parent_i


if __name__ == "__main__":
    h = Heap([(6, 54), (3, 23)])
    h.push(5, 67)
    h.push(4, 88)
    h.push(6, 55)
    h.push(1, 20)
    h.pop()
    print()
    print()
