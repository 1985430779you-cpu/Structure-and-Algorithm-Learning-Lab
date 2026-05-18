class Solution:
    def change(self, amount, coins):
        if amount == 0:
            return 1
        target = [0] * (amount+1)
        target[0] = 1
        for x in coins:
            for j in range(x, amount+1):
                target[j] += target[j-x]
        return target[-1]

coins = [1,2,5]
amount = 5
sol = Solution()
print(sol.change(amount,coins))