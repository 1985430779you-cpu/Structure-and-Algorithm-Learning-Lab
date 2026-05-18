class Solution:
    def maxAlternatingSum(self, nums):
        from functools import cache
        n = len(nums)

        @cache
        def dfs(i, mod):
            if i == n:
                return 0
            if mod:
                return max(dfs(i+1, True), dfs(i+1, False) + nums[i])
            else:
                return max(dfs(i+1, False), dfs(i+1, True) - nums[i])

        return dfs(0, True)
     
class Solution1:
    def maxAlternatingSum(self, nums):
        n = len(nums)
        dp = [[0]*2 for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            dp[i][0] = max(dp[i+1][0], dp[i+1][1] - nums[i])
            dp[i][1] = max(dp[i+1][1], dp[i+1][0] + nums[i])

        return dp[0][1]
    
nums = [4,2,5,3]
print(Solution1().maxAlternatingSum(nums))