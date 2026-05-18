class Solution:
    def countGoodStrings(self, low, high, zero, one):
        MOD = 1_000_000_007
        record = [0] * (high+1)
        record[0] = 1
        steps = [zero, one]
        for j in range(1, high+1):
            for i in steps:
                record[j] += record[j-i]

        return sum(record[low:high+1]) % MOD
    
low, high = 2, 3
zero, one = 1, 2
sol = Solution()
print(sol.countGoodStrings(low, high, zero, one))    