class Solution:           
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n <= 2:
            return min(cost)
        f0, f1 = 0, 0
        for i in range(2, n+1):
            f0, f1 = f1, min(cost[i-2]+f0, cost[i-1]+f1)
        return f1