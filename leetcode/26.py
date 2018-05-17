class Solution:
    def removeDuplicates(self, nums):
        if nums is None:
            return 0
        cnt = 0
        pre = None
        for numIndex in range(len(nums)):
            if nums[numIndex] == pre:
                nums[numIndex] = None
                cnt += 1
            else:
                pre = nums[numIndex]
        res = len(nums) - cnt
        for cntIndex in range(cnt):
            nums.remove(None)
        return res
