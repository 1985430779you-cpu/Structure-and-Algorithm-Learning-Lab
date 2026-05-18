class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[0]*(n+1) for _ in range(m+1)]
        for obj in strs:
            obj_m = obj.count("0")
            obj_n = obj.count("1")
            for x in range(m, obj_m-1, -1):
                for y in range(n, obj_n-1, -1):
                    dp[x][y] = max(dp[x][y], dp[x-obj_m][y-obj_n]+1)
        return dp[m][n]

strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(Solution().findMaxForm(strs, m, n))