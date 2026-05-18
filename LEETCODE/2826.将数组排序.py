class Solution:
    def minimumOperations(self, nums):
        n = len(nums)
        dp = [[0]*4 for _ in range(n+1)]
        for i, x in enumerate(nums):
            for j in range(1, 4):
                if j < x:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = max(dp[i][j], dp[i][x]+1)
        return n - dp[-1][3]
    
nums = [2,1,3,2,1]
print(Solution().minimumOperations(nums))