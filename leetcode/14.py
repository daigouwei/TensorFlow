class Solution:
    def longestCommonPrefix(self, strs):
        sortedStrs = sorted(strs, key=lambda x:len(x))
        sample = None
        if sortedStrs is not None and len(sortedStrs) != 0:
            sample = sortedStrs[0]
            sampleList = list(sample)
            for index in range(len(sampleList)):
                for str in sortedStrs:
                    if str[index] != sampleList[index]:
                        return sample[:index]
            return sample
        else:
            return ''

if __name__ == '__main__':
    hh = Solution().longestCommonPrefix(['123456','1235','124','12345'])
    print(hh)