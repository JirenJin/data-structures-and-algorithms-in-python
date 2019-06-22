"""Customized heap implementation in Python.

Supported operations:
- pop(): return the minimum key and the corresponding node, deleting them from the heap
- top(): return the minimum key and the corresponding node
- update_key(node, key): update the key (priority) of a node in the heap
- insert(node, key): insert node to the heap with the given key
- is_empty(): return True if heap is empty, otherwise return False
- heapify(list_of_nodes_and_keys): construct a heap from a list of nodes with given keys
"""


class Heap:
    def __init__(self):
        self._array = [None]
        self._node_to_index = {}
    
    @property
    def last(self):
        return len(self._array) - 1

    def is_empty(self):
        return len(self._array) == 1
    
    def top(self):
        return self._array[1]

    def pop(self):
        key, node = self._array[1]
        del self._node_to_index[node]
        self._array[1] = self._array[self.last]
        del self._array[self.last]
        self._sift_down(1)
        return key, node
    
    def update_key(self, node, key):
        index = self._node_to_index[node]
        curr_key = self._array[index]
        if key < curr_key:
            self._sift_up(index)
        elif key > curr_key:
            self._sift_down(index)
        
    def insert(self, node, key):
        self._array.append((key, node))
        self._node_to_index[node] = self.last
        self._sift_up(self.last)

    def _get_parent(self, index):
        return self._array[index // 2]

    def _get_left(self, index):
        return self._array[2 * index]

    def _get_right(self, index):
        return self._array[2 * index + 1]

    def _sift_up(self, index):
        curr_key, curr_node = self._array[index]
        while index >= 1 and curr_key < self._get_parent(index)[0]:
            self._array[index] = self._get_parent(index)
            self._node_to_index[self._get_parent(index)[1]] = index
            index = index // 2
        self._array[index] = curr_key, curr_node
        self._node_to_index[curr_node] = index

    def _sift_down(self, index):
        curr_key, curr_node = self._array[index]
        left = self._get_left(index)
        right = self._get_right(index)
        while index <= self.last and curr_key > left[0] or curr_key > right[0]:
            if left[0] <= right[0]:
                self._array[index] = left
                self._node_to_index[left[1]] = index
                index = 2 * index
            else:
                self._array[index] = right
                self._node_to_index[right[1]] = index
                index = 2 * index + 1
        self._array[index] = curr_key, curr_node
        self._node_to_index[curr_node] = index
