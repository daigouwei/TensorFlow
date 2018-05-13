# 这题目只能理解思路，但是程序实现上感觉有点吃力,所以程序实现上还是有问题

'''
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
'''
import sys


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # 必须保证对长度小的进行搜索，因为长度小的可能会越界
        if len(nums1) > len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
        leftIndex = 0
        rightIndex = len(nums1) * 2
        k = (len(nums1) + len(nums2)) // 2
        while leftIndex <= rightIndex:
            c1 = (leftIndex + rightIndex) // 2
            c2 = k - c1
            l1 = nums1[(c1 - 1) // 2] if c1 is not 0 else 0 - sys.maxsize
            r1 = nums1[c1 // 2] if c1 is not len(nums1) * 2 else sys.maxsize
            l2 = nums2[(c2 - 1) // 2] if c2 is not 0 else 0 - sys.maxsize
            r2 = nums2[c2 // 2] if c2 is not len(nums2) * 2 else sys.maxsize
            if l1 > r2:
                rightIndex = c1
            elif l2 > r1:
                leftIndex = c1
            else:
                break
        isOdd = self.checkOdd(len(nums1) + len(nums2))
        if isOdd:
            return max(r1, r2)
        else:
            return (max(l1, l2) + min(r1, r2)) / 2.0

    def checkOdd(self, len):
        if len % 2 == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4]
    nums2 = [4, 5, 6, 7, 7, 7]
    s = Solution()
    hh = s.findMedianSortedArrays(nums1, nums2)
    print(hh)
