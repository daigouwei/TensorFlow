'''
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
'''


class Solution:
    def threeSum(self, nums):
        resList = []
        if len(nums) < 3:
            return resList
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            # 去除重复的nus[i]
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            # 太大了
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            # 太小了
            if nums[i] + nums[k] + nums[k - 1] < 0:
                continue
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif sum > 0:
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    resList.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
        return resList


if __name__ == '__main__':
    hh = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print(hh)
