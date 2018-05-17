class Solution:
    def searchInsert(self, nums, target):
        if nums is None or len(nums) == 0:
            return 0
        try:
            return nums.index(target)
        except Exception:
            if target > nums[-1]:
                return len(nums)
            elif target < nums[0]:
                return 0
            else:
                left = 0
                right = len(nums) - 1
                mid = (left + right) // 2
                while True:
                    if target > nums[mid]:
                        left = mid
                    elif target < nums[mid]:
                        right = mid
                    if abs(right - left) == 1:
                        return max(right, left)


if __name__ == '__main__':
    hh = Solution().searchInsert([1, 2, 4, 6, 7], 3)
    print(hh)
