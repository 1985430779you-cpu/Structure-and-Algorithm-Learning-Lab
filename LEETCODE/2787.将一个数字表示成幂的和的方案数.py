class Solution:
    def numberOfWays(self, n, x):
        MOD = 1000000007
        target = int(n**(1/x))
        nums = [i**x for i in range(1, target+2)]
        record = [0] * (n+1)
        record[0] = 1
        for i in nums:
            for j in range(n, i-1, -1):
                record[j] += record[j-i]
        return record[n] % MOD      
    
n = 64
x = 3
sol = Solution()
print(sol.numberOfWays(n, x))