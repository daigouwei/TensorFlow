# 不太好的思路：复杂度为O(n2)，使用两个for循环从最大数量值开始截取，如果去重后数量和不去重数量一致就找到最大的没有重复字符的子串个数
# 牛逼的思路：复杂度为O(n)，遍历整个str，对字符进行map处理，每次拿到字符最后一次地址和前一个没有重复的地址做减法得到结果。这里不要担心减法
# 的时候中间冲入了其他重复的字符，减数是一个最接近被减数的无重复的字符。这里思路的关键就是要设置到减数的地址移动。

'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        sLen = len(s)
        for chunkLen in range(sLen, 0, -1):
            for index in range(sLen - chunkLen + 1):
                str = s[index:index + chunkLen]
                if self.uniq(str) == chunkLen:
                    return chunkLen
        return 0

    def uniq(self, str):
        strL = list(str)
        uniqStrL = list(set(strL))
        return len(uniqStrL)
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        if s is None or len(s) == 0:
            return 0
        d = {}
        start = 0
        preRes = 0
        for index in range(len(s)):
            if s[index] in d and d[s[index]] >= start:
                start = d[s[index]] + 1
            res = index - start + 1
            d[s[index]] = index
            preRes = max(preRes, res)
        return preRes


if __name__ == '__main__':
    s = Solution()
    cnt = s.lengthOfLongestSubstring("abbbcabahec")
    print(cnt)
