class Solution:
    def strStr(self, haystack, needle):
        if needle is None or needle == '':
            return 0
        for index in range(len(haystack) - len(needle) + 1):
            if haystack[index] == needle[0]:
                if haystack[index: index + len(needle)] == needle:
                    return index
        return -1
