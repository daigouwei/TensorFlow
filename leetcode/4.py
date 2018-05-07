class MergeSort:
    def mergeArr(self, a, b):
        lenA = len(a)
        lenB = len(b)
        c = []
        indexA = indexB = 0
        while indexA < lenA and indexB < lenB:
            if a[0] < b[0]:
                c.append(a[0])
                del a[0]
                indexA += 1
            else:
                c.append(b[0])
                del b[0]
                indexB += 1
        c.extend(a)
        c.extend(b)
        return c


if __name__ == '__main__':
    c = MergeSort().mergeArr([1, 2, 4], [2, 3, 5, 7])
    print(c)
