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
'''

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i+1
                right = len(nums)-1
                if nums[i]+nums[i+1]+nums[i+2]>0:
                        break
                if nums[i]+nums[right]+nums[right-1]<0:
                        continue
                while left < right:
                    ident = nums[left] + nums[right] + nums[i]
                    if ident == 0:
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1; right -= 1
                        while left < right and nums[left] == nums[left-1]:    # skip duplicates
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif ident < 0:
                        left += 1
                    else:
                        right -= 1
        return ans

if __name__ == '__main__':
    hh = Solution().threeSum([-1, 0, 1])
    print(hh)
