class Solution:
    def twoSum(self, nums, target):
        d = {}
        for index in range(len(nums)):
            d[nums[index]] = index
        for index1 in range(len(nums)):
            val = target - nums[index1]
            if val in d.keys() and index1 is not d[val]:
                index2 = d[val]
                return [index1, index2]


if __name__ == '__main__':
    s = Solution()
    [i, j] = s.twoSum([3, 3], 6)
    print([i, j])
