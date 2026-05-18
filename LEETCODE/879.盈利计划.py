class Solution:
    def profitableSchemes(self, n, minProfit, group, profit):
        MOD = 10**9+7
        target = sum(profit)
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1

        for x, v in zip(group, profit):
            for i in range(n, x-1, -1):
                for j in range(target, v-1, -1):
                    dp[i][j] += dp[i-x][j-v]
        
        ans = 0
        for i in range(n + 1):
            for j in range(minProfit, target + 1):
                ans = (ans + dp[i][j]) % MOD

        return ans

n = 5
minProfit = 3
group = [2,2] 
profit = [2,3]
print(Solution().profitableSchemes(n, minProfit, group, profit))