class Solution:
    def myAtoi(self, str):
        usefulChar = []
        isFirstChar = True
        for s in str:
            if s is not ' ':
                if isFirstChar:
                    isFirstChar = False
                    if s is '-' or s is '+' or (s >= '0' and s <= '9'):
                        usefulChar.append(s)
                    else:
                        break
                else:
                    if s >= '0' and s <= '9':
                        usefulChar.append(s)
                    else:
                        break
            else:
                if isFirstChar is False:
                    break
        if len(usefulChar) is 0:
            return 0
        else:
            if len(usefulChar) is 1 and (usefulChar[0] is '-' or usefulChar[0] is '+'):
                return 0
        num = 0
        if usefulChar[0] is not '-' and usefulChar[0] is not '+':
            num = self.convertStr2Num(''.join(usefulChar))
            if num >= 2 ** 31 - 1:
                return 2 ** 31 - 1
        elif usefulChar[0] is '-':
            num = 0 - self.convertStr2Num(''.join(usefulChar[1:]))
            if num <= -2 ** 31:
                return -2 ** 31
        elif usefulChar[0] is '+':
            num = self.convertStr2Num(''.join(usefulChar[1:]))
            if num >= 2 ** 31 - 1:
                return 2 ** 31 - 1
        return num

    def convertStr2Num(self, str):
        nums = []
        for s in str:
            nums.append(ord(s) - ord('0'))
        number = 0
        for index in range(len(nums)):
            number += nums[index] * 10 ** (len(nums) - 1 - index)
        return number


if __name__ == '__main__':
    hh = Solution().myAtoi('+1')
    print(hh)
