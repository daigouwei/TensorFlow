class Solution:
    def generate(self, numRows):
        l = [[1]]
        for i in range(1, numRows):
            l1 = [0]
            l2 = l.copy()[i-1].copy()
            l1.extend(l[i - 1])
            l2.extend([0])
            l.append([l1[j]+l2[j] for j in range(len(l1))])
        return l


if __name__ == '__main__':
    hh = Solution().generate(1)
    print(hh)
