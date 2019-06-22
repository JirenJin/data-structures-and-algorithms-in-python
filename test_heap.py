import heapq
import random

import heap


def test_heap():
    heap_queue = heap.Heap()
    builtin_heap = []
    for node in range(10000):
        if heap_queue.is_empty():
            assert not builtin_heap 
        else:
            assert heap_queue.top()[0] == builtin_heap[0][0]
        key = random.randint(0, 1000)
        heap_queue.insert(node, key)
        heapq.heappush(builtin_heap, (key, node))
        assert heap_queue.top()[0] == builtin_heap[0][0]
        if not heap_queue.is_empty():
            if random.random() > 0.5:
                key1, _ = heap_queue.pop()
                key2, _ = heapq.heappop(builtin_heap)
                assert key1 == key2