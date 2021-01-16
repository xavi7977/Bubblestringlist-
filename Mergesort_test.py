Mergesort_test.py
import timeit


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if len(left[i]) <= len(right[j]):
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result += left[i:]
    result += right[j:]
    return result


def test1(nlist=["Xavier","Galarza","Henny"]):
    if len(nlist) > 1:
        mid = len(nlist) // 2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        test1(lefthalf)
        test1(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k] = lefthalf[i]
                i = i + 1
            else:
                nlist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            nlist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            nlist[k] = righthalf[j]
            j = j + 1
            k = k + 1
        return nlist


if __name__ == '__main__':
    print(timeit.timeit("test1()", setup="from __main__ import test1"))
