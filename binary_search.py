def bisect_right(array, x, low=0, high=None):
    if low < 0:
        raise ValueError('low should be a non-negative integer.')
    if high is None:
        high = len(array) - 1
    else:
        if high > len(array) - 1:
            raise ValueError(f'high should be less than len(array): {len(array)}.')
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] <= x:
            low = mid + 1
        else:
            high = mid - 1
    return low


def bisect_left(array, x, low=0, high=None):
    if low < 0:
        raise ValueError('low should be a non-negative interger.')
    if high is None:
        high = len(array) - 1
    else:
        if high > len(array) - 1:
            raise ValueError(f'high should be less than len(array): {len(array)}.')
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return low


def binary_search_left(array, x):
    index = bisect_left(array, x)
    if index != len(array) and array[index] == x:
        return index
    raise ValueError


def binary_search_right(array, x):
    index = bisect_right(array, x)
    if index != 0 and array[index - 1] == x:
        return index
    raise ValueError


if __name__ == "__main__":
    import bisect
    import random
    for _ in range(1000):
        a = [random.randint(0, 10) for _ in range(100)]
        a.sort()
        x = bisect_right(a, 5) 
        y = bisect.bisect_right(a, 5)
        assert x == y

    for _ in range(1000):
        a = [random.randint(0, 10) for _ in range(100)]
        a.sort()
        x = bisect_left(a, 5) 
        y = bisect.bisect_left(a, 5)
        assert x == y
