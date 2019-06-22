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

    def __repr__(self):
        return repr(self._array[1:])
    
    @property
    def last(self):
        return len(self._array) - 1

    def is_empty(self):
        return len(self._array) == 1
    
    def top(self):
        if self.is_empty():
            return None
        return self._array[1]

    def pop(self):
        if self.is_empty():
            return None
        key, node = self._array[1]
        del self._node_to_index[node]
        self._array[1] = self._array[self.last]
        del self._array[self.last]
        if not self.is_empty():
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
        if index == 1:
            return None
        return self._array[index // 2]

    def _get_left(self, index):
        if 2 * index > self.last:
            return None
        return self._array[2 * index]

    def _get_right(self, index):
        if 2 * index + 1 > self.last:
            return None
        return self._array[2 * index + 1]

    def _get_smaller_child_index(self, index, curr_key):
        left = self._get_left(index)
        right = self._get_right(index)
        if left is None:
            return None
        if right is None or left[0] <= right[0]:
            return 2 * index if left[0] < curr_key else None
        else: 
            return 2 * index + 1 if right[0] < curr_key else None 

    def _sift_up(self, index):
        curr_key, curr_node = self._array[index]
        while index > 1 and curr_key < self._get_parent(index)[0]:
            self._array[index] = self._get_parent(index)
            self._node_to_index[self._get_parent(index)[1]] = index
            index = index // 2
        self._array[index] = curr_key, curr_node
        self._node_to_index[curr_node] = index

    def _sift_down(self, index):
        curr_key, curr_node = self._array[index]
        smaller_child_index = self._get_smaller_child_index(index, curr_key)
        while smaller_child_index is not None:
            smaller_child = self._array[smaller_child_index]
            self._array[index] = smaller_child
            self._node_to_index[smaller_child[1]] = index
            index = smaller_child_index
            smaller_child_index = self._get_smaller_child_index(index, curr_key)
        self._array[index] = curr_key, curr_node
        self._node_to_index[curr_node] = index
