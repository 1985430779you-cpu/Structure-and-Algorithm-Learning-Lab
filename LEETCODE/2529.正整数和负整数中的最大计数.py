class Solution:
    def maximumCount(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        low = 0
        high = n-1
        if nums[low] == nums[high] == 0:
            return 0
        if nums[low] > 0 or nums[high] < 0:
            return n
        while low < high:
            mid = (low+high) // 2
            if nums [mid] >= 0:
                high = mid 
            else:
                low = mid + 1
        left = low
        
        low = 0
        high = n-1
        while low < high:
            mid = (low+high) // 2
            if nums [mid] >= 1:
                high = mid
            else:
                low = mid + 1
        right = low - 1

        return max(left, n-1-right)
    
nums = []
sol = Solution()
print(sol.maximumCount(nums))