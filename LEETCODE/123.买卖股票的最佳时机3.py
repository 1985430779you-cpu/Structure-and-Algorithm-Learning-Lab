class Solution:
    def maxProfit(self, prices):
        from functools import cache
        n = len(prices)

        @cache
        def dfs(day, hold, num):
            if num < 0:
                return -float("inf")
            if day < 0:
                return -float("inf") if hold else 0
            if hold:
                return max(dfs(day-1, True, num), dfs(day-1, False, num-1)-prices[day])
            else:
                return max(dfs(day-1, False, num), dfs(day-1, True, num)+prices[day])
        
        return dfs(n-1, False, 2)
    
class Solution1:
    def maxProfit(self, prices):
        n = len(prices)
        dis = [[[-float("inf")]*2 for _ in range(n+1)] for _ in range(2+2)]
        for num in range(1, 4):
            dis[num][0][0] = 0

        for num in range(1, 4):
            for i, p in enumerate(prices):
                dis[num][i+1][0] = max(dis[num][i][0], dis[num][i][1]+p)
                dis[num][i+1][1] = max(dis[num][i][1], dis[num-1][i][0]-p)
        return dis[-1][n][0]
    
prices = [3,3,5,0,0,3,1,4]
print(Solution1().maxProfit(prices))