class Solution:
    def minOperations(self, nums, x):
        n = len(nums)
        if n <= 0:
            return -1
        if x == 0:
            return 0
        if x < min(nums):
            return -1
        
        s = sum(nums)
        total = 0
        ans = -1
        i = 0
        for j in range(n):
            total += nums[j]
            
            while total > s-x and i <= j:
                total -= nums[i]
                i += 1

            if total == s-x:
                ans = max(ans, j-i+1)

        return ans if ans == -1 else n-ans
    
nums = [1,1,4,2,3]
x = 5
sol = Solution()
print(sol.minOperations(nums, x))    