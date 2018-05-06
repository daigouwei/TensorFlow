class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        numList = []
        while x > 0:
            num = x % 10
            x = x // 10
            numList.append(num)
        for index in range(round(len(numList) / 2)):
            if numList[index] != numList[len(numList) - 1 - index]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    hh = s.isPalindrome(123321)
    print(hh)
