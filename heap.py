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
    """A customized heap implementation supporting update of keys.

    The main motivation to implement a customized heap instead of using the 
    builtin `heapq` module is due to the need for efficiently updating and 
    deleting an arbitrary node in the heap.

    Attributes:
        _array: an array actually storing the keys and nodes.
        _node_to_index: a hashmap from node to its index in the heap (`_array`)
        last: the index of the last node in the heap, also representing the
            current size of the heap.
    """
    def __init__(self):
        """Inits the hidden array and the mapping from node to index.
        
        Note that `_array` stores actual elements from index `1`, i.e., the 
        value at `0` index does not matter.
        """
        self._array = [None]
        self._node_to_index = {}

    def __repr__(self):
        """Returns the array representation of the heap."""
        return repr(self._array[1:])
    
    @property
    def last(self):
        """Index of the last element/node in the heap."""
        return len(self._array) - 1

    def is_empty(self):
        """Returns True if the heap is empty, otherwise False."""
        # the actual heap elements starts from `1` index 
        return len(self._array) == 1
    
    def top(self):
        """Returns the (key, node) tuple of the minimum / top of the heap.
        
        If the heap is empty, returns None.
        """
        if self.is_empty():
            return None
        return self._array[1]

    def pop(self):
        """Returns and deletes the (key, node) tuple from the top of the heap.
        
        If the heap is empty, does nothing and returns None.
        """
        if self.is_empty():
            return None
        key, node = self._array[1]
        del self._node_to_index[node]
        self._array[1] = self._array[self.last]
        del self._array[self.last]
        # no need to sift down if the heap is already empty
        if not self.is_empty():
            self._sift_down(1)
        return key, node
    
    def update_key(self, node, key):
        """Updates the key for the given node in the heap.

        After updating the key, this function ensures that the heap property is
        maintained.
        """
        index = self._node_to_index[node]
        curr_key, _ = self._array[index]
        self._array[index] = (key, node)
        if key < curr_key:
            self._sift_up(index)
        elif key > curr_key:
            self._sift_down(index)
        
    def insert(self, node, key):
        """Inserts a new node with the given key to the heap."""
        self._array.append((key, node))
        self._node_to_index[node] = self.last
        self._sift_up(self.last)

    def _get_parent(self, index):
        """Returns the parent (key, node) tuple for the given index.
        
        Returns None if the index is 1, i.e., the index of the top of the heap.
        """
        if index == 1:
            return None
        return self._array[index // 2]

    def _get_left(self, index):
        """Returns the left child of the given index.

        Returns None is the left child does not exists. 
        """
        if 2 * index > self.last:
            return None
        return self._array[2 * index]

    def _get_right(self, index):
        """Returns the right child of the given index.

        Returns None is the right child does not exists. 
        """
        if 2 * index + 1 > self.last:
            return None
        return self._array[2 * index + 1]

    def _get_smaller_child_index(self, index, curr_key):
        """Returns the index of the child that has a smaller key than curr_key.

        The key of this child should also be smaller than or equal to the other 
        child of the node with `index`. 
        If there is not such a child, returns None.
        """
        left = self._get_left(index)
        right = self._get_right(index)
        if left is None:
            return None
        if right is None or left[0] <= right[0]:
            return 2 * index if left[0] < curr_key else None
        else: 
            return 2 * index + 1 if right[0] < curr_key else None 

    def _sift_up(self, index):
        """Sift up a node until the parent's key is not larger than its key.

        Siftting up means swapping the parent and current node when necessary.
        Note that the `_node_to_index` hashmap should also be updated during
        the sifting procedure.
        """
        if index < 1:
            raise IndexError("index should be larger than 0.")
        curr_key, curr_node = self._array[index]
        while index > 1 and curr_key < self._get_parent(index)[0]:
            self._array[index] = self._get_parent(index)
            self._node_to_index[self._get_parent(index)[1]] = index
            index = index // 2
        self._array[index] = curr_key, curr_node
        self._node_to_index[curr_node] = index

    def _sift_down(self, index):
        """Sift down a node until the children's keys are not larger than its.

        Siftting down means swapping the current node and one of its children 
        with the smaller key when necessary. Note that the `_node_to_index`
        hashmap should also be updated during the sifting procedure.
        """
        if index > self.last:
            raise IndexError("index is out of boundary")
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