class Solution:
    def numSquares(self, n):
        import math
        target = int(math.sqrt(n))
        nums = [i**2 for i in range(target+1)]
        record = [math.inf] * (n+1)
        record[0] = 0
        for x in nums:
            for j in range(x, n+1):
                record[j] = min(record[j], record[j-x]+1)
        return record[n]
    
n = 112
sol = Solution()
print(sol.numSquares(n))