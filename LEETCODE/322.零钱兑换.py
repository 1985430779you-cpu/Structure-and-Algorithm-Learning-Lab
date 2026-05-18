class Solution:
    def cashChange(self, coins, amount):
        n = len(coins)
        if amount == 0 and n <= 0:
            return 0
        import math
        record = [math.inf] * (amount+1)
        record[0] = 0

        for x in coins:
            for j in range(x, amount+1):
                record[j] = min(record[j], record[j-x]+1)       
        return record[-1] if record[-1] < math.inf else -1
    
coins = [1, 2, 5]
amount = 11
sol = Solution()
print(sol.cashChange(coins, amount))