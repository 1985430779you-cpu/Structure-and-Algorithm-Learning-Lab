class Solution:
    def maxProfit(self, prices):
        from functools import cache
        n = len(prices)

        @cache
        def dfs(day, hold):
            if day == -1:
                return -float("inf") if hold == 1 or hold == -1 else 0
            if hold == 1:
                return max(dfs(day-1, 1), dfs(day-1, 0) - prices[day])
            elif hold == -1:
                return dfs(day-1, 1) + prices[day]
            else:
                return max(dfs(day-1, 0), dfs(day-1, -1))
            
        return max(dfs(n-1, 0), dfs(n-1, -1))
    
class Solution1:
    def maxProfit(self, prices):
        n = len(prices)
        dis = [[0]*3 for _ in range(n)]
        dis[0][0] = 0
        dis[0][1] = -prices[0]
        dis[0][2] = 0
        for i in range(1, n):
            dis[i][2] = dis[i-1][1] + prices[i]
            dis[i][0] = max(dis[i-1][0], dis[i-1][2])
            dis[i][1] = max(dis[i-1][1], dis[i-1][0] - prices[i])
        return max(dis[-1][0], dis[-1][2])

prices = [1,2,3,0,2]
print(Solution1().maxProfit(prices))