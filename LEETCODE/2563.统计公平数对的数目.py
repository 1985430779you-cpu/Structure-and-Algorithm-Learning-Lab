class Solution:
    def countFairPairs(self, nums, lower, upper):
        n = len(nums)
        if n == 0:
            return 0

        nums.sort()
        ans = 0
        l = r = n-1
        for j in range(len(nums)):
            while r > upper - nums[j]:
                r -= 1
            while l >= lower - nums[j]:
                l -= 1
            ans += min(r,j) - min(l,j)
        return ans
    
class Solution1:
    def countFairPairs(self, nums, lower, upper):
        n = len(nums)
        if n == 0:
            return 0
        
        nums.sort()
        ans = 0

        for j in range(n-1):
            left, right = j+1, n-1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] >= upper - nums[j] + 1:
                    right = mid - 1
                else:
                    left = mid + 1
            high = left-1

            left, right = j+1, n-1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] >= lower - nums[j]:
                    right = mid - 1
                else:
                    left = mid + 1
            low = left

            ans += high-low+1
        return ans
    
class Solution:
    def countFairPairs(self, nums, lower, upper):
        import bisect
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n-1): #切片会增加时间复杂度，用函数自带功能限定范围
            ans += bisect.bisect_right(nums, upper-nums[i], i+1, n) - bisect.bisect_left(nums, lower-nums[i], i+1, n)
        return ans

nums = [0,0,0,0,0,0]
lower = 0
upper = 0
sol = Solution1()
print(sol.countFairPairs(nums, lower, upper))