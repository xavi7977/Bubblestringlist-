import timeit

def test1(lst=["Xavier","Galarza","Henny"]):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst


if __name__ == '__main__':
    print(timeit.timeit("test1()", setup="from __main__ import test1"))

