class Solution:
    def threeSum(self, nums):
        resList = []
        if len(nums) < 3:
            return resList
        nums.sort()
        preI = None
        preJ = None
        for i in range(len(nums) - 2):
            if preI == nums[i]:
                continue
            preI = nums[i]
            for j in range(i + 1, len(nums) - 1):
                if preJ == nums[j]:
                    continue
                preJ = nums[j]
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        resList.append([nums[i], nums[j], nums[k]])
                        break
        return resList


if __name__ == '__main__':
    hh = Solution().threeSum([-1,0,1,2,-1,-4])
    print(hh)
