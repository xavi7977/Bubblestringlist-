Quicksort_test.py
import timeit


def test1(array=["Xavier","Galarza","Henny"]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return test1(less) + equal + test1(greater)
    else:
        return array


if __name__ == '__main__':
    print(timeit.timeit("test1()", setup="from __main__ import test1"))
