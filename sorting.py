"""This module implements common sorting functions."""


# time: O(n^2) | space: O(1), in-place sorting
def insertion_sort(array):
    for i in range(1, len(array)):
        to_sort = array[i]
        # for j in range(i, -1, -1):
        #     if to_sort < array[j-1]:
        #         array[j] = array[j-1]
        #     else:
        #         break
        # array[j] = to_sort
        j = i - 1
        while j >= 0 and to_sort < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = to_sort
    return array


if __name__ == "__main__":
    import random
    testcases = [[random.randint(0, 100) for _ in range(10)] for _ in range(100)]
    for i, testcase in enumerate(testcases):
        if sorted(testcase[:]) != insertion_sort(testcase):
            print(testcases[i], testcase, sorted(testcase[i])) 
            break
    print("All test cases passed!")