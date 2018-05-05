class Solution:
    def twoSum(self, nums, target):
        len = nums.__len__()
        for i in range(len):
            for j in range(i+1, len):
                if nums[i]+nums[j] == target:
                    return [i,j]

if __name__ == '__main__':
    s = Solution();
    [i,j] = s.twoSum([1,2,3,4], 6)
