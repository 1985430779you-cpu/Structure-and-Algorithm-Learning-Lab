class Solution:
    def maxScore(self, nums, x):
        from functools import cache
        n = len(nums)

        @cache
        def dfs(i, m):
            if i == n:
                return 0
            if nums[i] % 2 == m:
                return max(dfs(i+1, m)+nums[i], dfs(i+1, m^1)+nums[i]-x)
            else:
                return dfs(i + 1, m)

        return dfs(0, nums[0] % 2)
   
class Solution1:
    def maxScore(self, nums, x):
        n = len(nums)
        dp = [[0]*2 for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            m = nums[i] % 2
            dp[i][m] = max(dp[i+1][m] + nums[i], dp[i+1][m^1]+nums[i]-x)
            dp[i][m^1] = dp[i+1][m^1]
        
        return dp[0][nums[0]%2]

nums = [2,3,6,1,9,2]
x = 5
print(Solution1().maxScore(nums, x))