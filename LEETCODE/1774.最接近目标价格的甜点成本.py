class Solution:
    def closestCost(self, baseCosts, toppingCosts, target):
        ans = min(baseCosts)
        cloest = target
        dp = [False for _ in range(target*2+1)]

        for x in baseCosts:
            if x < 2*target:
                dp[x] = True

        for y in toppingCosts:
            for cost in range(2*target, y-1, -1):
                dp[cost] = dp[cost] or dp[cost-y]
                if cost > 2*y and dp[cost-2*y]:
                    dp[cost] = True

        for cost in range(1, 2*target+1):
            if dp[cost]:
                c = abs(target-cost)
                if c < cloest:
                    cloest = c
                    ans = cost
        return ans        

baseCosts = [2,3]
toppingCosts = [4,5,100]
target = 18
print(Solution().closestCost(baseCosts, toppingCosts, target))