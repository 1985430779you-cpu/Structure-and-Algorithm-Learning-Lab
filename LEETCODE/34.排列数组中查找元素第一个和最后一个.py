class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        
        #应用>=和<=找出某个数字的起始和终止位置
        low, high = -1, len(nums)
        while low+1 < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid
            elif nums[mid] >= target:
                high = mid
        start = high

        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        low, high = -1, len(nums)
        while low+1 < high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid
            else:
                high = mid
        end = low

        return start, end
    
nums = [5, 7, 7, 8, 8, 8, 8, 10]
target = 7
sol = Solution()
print(sol.searchRange(nums, target))        