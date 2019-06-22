import heapq
import random

import heap


def test_heap_insert_update_pop_top():
    """Test for insert, update_key, pop and top methods of the `Heap` class.

    Note that `heapq` module will use the tuple (key, node) together as the
    actual key, and we also need to use both as actual keys to make sure the
    popped nodes are the same for the builtin and customized heap.
    """
    heap_queue = heap.Heap()
    builtin_heap = []
    for node in range(10000):
        if heap_queue.is_empty():
            assert not builtin_heap 
        else:
            # we compare the actual key used: (key, node) tuple
            assert heap_queue.top()[0] == builtin_heap[0]
        key = random.randint(0, 1000)
        heap_queue.insert(node, (key, node))
        heapq.heappush(builtin_heap, (key, node))
        assert heap_queue.top()[0] == builtin_heap[0]
        if not heap_queue.is_empty():
            if random.random() > 0.5:
                assert heap_queue.pop()[0] == heapq.heappop(builtin_heap)