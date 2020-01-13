from typing import Tuple, List, Dict, Any
from .exceptions import UnexpectedPriority, DuplicatesEnabled, BadData, DuplicateInputs


class HeapQueue:
    def __init__(self, data: List = None, duplicates: bool = False, priorities: bool = True):
        self._array: List[Tuple[Any, Any]] = []
        self._positions: Dict[Any, int] = {}
        self._duplicates: bool = duplicates
        self._priorities: bool = priorities
        self.size: int = 0
        if data is not None:
            self._process_data(data)
            self._array = data
            self.size = len(self._array)
            self._heapify()

    def push(self, priority, value=None) -> None:  # will also update priority if already in the heap
        """
        Pushes an element onto the heap by placing at the bottom and sifting up in O(logn) time.
        Will also update the priority of existing elements if priorities exist and positions are
        being tracked.
        """
        if not self._priorities:
            if value is not None:
                raise UnexpectedPriority
            value = priority
        if not self._duplicates and value in self._positions:  # updates priority if value already in heap
            position = self._positions[value]
            if priority > self._array[position][0]:
                self._array[position] = (priority, self._array[position][1])
                self._heapify_down(position)
            elif priority < self._array[position][0]:
                self._array[position] = (priority, self._array[position][1])
                self._heapify_up(position)
        else:  # otherwise add the new element
            if not self._duplicates:
                self._positions[value] = self.size
            self._array.append((priority, value))
            self.size += 1
            self._heapify_up(self.size - 1)

    def remove(self, value) -> Tuple[Any, Any]:
        """Removes the node corresponding to the value if it is in the heap. Takes O(logn) time"""
        if not self._duplicates:
            try:
                position: int = self._positions[value]
            except KeyError:
                raise KeyError(value)
            else:
                return self._delete(position)
        else:
            raise DuplicatesEnabled

    def pop(self) -> Tuple[Any, Any]:
        """Returns the element at the root fo the heap and removes it. O(logn) time"""
        return self._delete(0)

    def peek(self) -> Tuple[Any, Any]:
        """Returns the element at the root of the heap while keeping it in the heap. O(1) time"""
        return self._array[0]

    def get_priority(self, value) -> Any:
        """
        Gets the priority of a given value in the heap in O(1) time.
        Raises appropriate key error if it's not in the heap.
        """
        if not self._duplicates:
            return self._array[self._positions[value]][0]
        else:
            raise DuplicatesEnabled

    def exists(self, value) -> bool:
        """Checks if a given value is in the heap. O(1) time"""
        # Todo: decide if lookups with duplicates enabled should be allowed since it will be O(n) instead of O(1)
        if not self._duplicates:
            return value in self._positions
        # else:
        #     raise DuplicatesEnabled
        else:
            for element in self._array:  # todo: check speedup with DFS, or checking entire row is greater than
                if element[1] == value:
                    return True
            return False

    def extend(self, data: List):
        """
        Efficiently extends the heap while maintaining the heap property. Takes O(nlogn) time.
        This is faster than looping through elements and pushing onto the heap as the heap's
        array only needs to be extended once using the inbuilt Python method taking advantage of
        it's C implementation.
        """
        data_size = len(data)
        old_size = self.size
        self._array.extend(data)
        self._process_data(self._array, old_size)
        self.size = self.size + data_size

        for i in range(old_size, self.size):
            self._heapify_up(i)

    def _process_data(self, data: List, start_index: int = 0):
        """
        Checks and converts input data depending on properties set (duplicates/priorities enabled/disabled)
        This takes O(n) time, and at most O(n) extra space
        """
        size = len(data)

        for i in range(start_index, size):  # checks that elements are in correct format of (priority, value)
            if not self._priorities:
                data[i] = (data[i], data[i])
            elif not isinstance(data[i], Tuple):
                raise BadData
            elif len(data[i]) != 2:
                raise BadData
            if not self._duplicates:
                if data[i][1] in self._positions:  # should it automatically remove duplicates? (if so how)
                    raise DuplicateInputs
                else:
                    self._positions[data[i][1]] = i

    def _heapify(self) -> None:
        """Inplace manipulation of the heap resulting in a satisfied heap property in O(nlogn) time"""
        for i in reversed(range(self.size // 2)):
            self._heapify_down(i)

    def _delete(self, i: int) -> Tuple[Any, Any]:
        """Deletes the element at a given index while maintaining the heap property in O(logn) time"""
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
        """Moves element down the heap until its children are larger, or becomes a leaf. O(logn) time"""
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
        """Swaps element with parent until parent is smaller or reaches root. O(logn) time"""
        while i > 0:
            parent_index: int = (i - 1) >> 1
            if not self._swap(parent_index, i):
                break
            i = parent_index

    def _swap(self, parent_index: int, child_index: int) -> bool:
        """
        Checks if the two elements should be swapped and swaps in O(1) time.
        Returns True/False depending if a swap happens or not.
        """
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
