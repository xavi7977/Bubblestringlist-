Bubblestringlist.py
class BubbleStringList:
    def __init__(self):
        self.list = []

    def add(self, input):
        self.list.append(input)

    def sort(self, lst):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[j] < lst[i]:
                    lst[j], lst[i] = lst[i], lst[j]
        return list


class MergeStringList:
    def __init__(self):
        self.list = []

    def add(self, input):
        self.list.append(input)

    def merge(self, left, right):
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

    def sort(self, nlist):
        if len(nlist) > 1:
            mid = len(nlist) // 2
            lefthalf = nlist[:mid]
            righthalf = nlist[mid:]

            self.sort(lefthalf)
            self.sort(righthalf)
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


class QuickStringList:
    def __init__(self):
        self.list = []

    def add(self, input):
        self.list.append(input)

    def sort(self, array):
        """Sort the array by using quicksort."""

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
            
            return self.sort(less)+ equal + self.sort(greater)
        else:  
            return array
        if __name__ == '__main__':
            b = BubbleStringList()
        b.add("Xavier")
        b.add("Galarza")
        b.add("Jose")
        b.add("Randy")
        b.add("Henny")
        b.sort(b.list)
        print(b.list)

        c =MergeStringList()
        c.add("Xavier")
        c.add("Galarza")
        c.add("Jose")
        c.add("Randy")
        c.add("Henny")
        c.sort(c.list)
        print(c.list)

        q = QuickStringList()
        q.add("Xavier")
        q.add("Galarza")
        q.add("Jose")
        q.add("Randy")
        q.add("Henny")
        print(q.sort(q.list))
