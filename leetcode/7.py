class Solution:
    def reverse(self, x):
        list = []
        if x < 0:
            xx = 0 - x
            isPositive = False
        else:
            xx = x
            isPositive = True
        while xx > 0:
            list.append(xx % 10)
            xx = xx // 10
        sum = 0
        for index in range(len(list)):
            sum += list[index] * 10 ** (len(list) - 1 - index)
        if isPositive:
            if sum >= -2 ** 31 and sum <= 2 ** 31 - 1:
                return sum
            else:
                return 0
        else:
            if 0 - sum >= -2 ** 31 and 0 - sum <= 2 ** 31 - 1:
                return 0 - sum
            else:
                return 0


if __name__ == '__main__':
    hh = Solution().reverse(1534236469)
    print(hh)
