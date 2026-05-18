class Solution:
    def sumOfPower(self, nums, k):
        mod = 10**9+7
        n = len(nums)
        #dp = [[0]*(k+1) for _ in range(n+1)]
        dp = [[] for _ in range(k+1)] 
        dp[0].append(0)  
        
        for x in nums:        
            for i in range(k, x-1, -1):
                for value in dp[i-x]:
                    dp[i].append(value+1)
        
        ans = 0
        if not dp[k]:
            return ans
        for i in dp[k]:
            ans = (ans + 2**(n-i)) % mod
        return ans
    
class Solution1:
    def sumOfPower(self, nums, k):
        mod = 10**9+7
        n = len(nums)
        dp = [[0]*(n+1) for _ in range(k+1)]
        dp[0][0] = 1   
        
        for _, x in enumerate(nums):        
            for i in range(k, x-1, -1):
                for j in range(n, 0, -1):
                    dp[i][j] += dp[i-x][j-1]

        ans = 0
        for i in range(1, n+1):
            if dp[k][i]:
                ans = (ans + dp[k][i]*2**(n-i)) % mod
        return ans

nums = [2,3,3]
k = 5
print(Solution1().sumOfPower(nums, k))