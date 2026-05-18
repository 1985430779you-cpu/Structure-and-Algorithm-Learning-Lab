class Solution:
    def maxProfit(self, prices):
        from functools import cache
        n = len(prices)

        @cache
        def dfs(day, hold):
            if day == -1:
                return -float("inf") if hold else 0
            if hold:
                return max(dfs(day-1, True), dfs(day-1, False) - prices[day])
            else:
                return max(dfs(day-1, False), dfs(day-1, True) + prices[day])

        return dfs(n-1, False)
    
class Solution1:
    def maxProfit(self, prices):
        n = len(prices)
        dis = [[0]*2 for _ in range(n+1)]
        dis[0][0] = 0
        dis[0][1] = -float("inf")
        for i in range(1, n+1):
            dis[i][0] = max(dis[i-1][0], dis[i-1][1] + prices[i-1])
            dis[i][1] = max(dis[i-1][1], dis[i-1][0] - prices[i-1])
        return dis[n][0]
    
prices = [1,2,3,4,5]
print(Solution().maxProfit(prices))