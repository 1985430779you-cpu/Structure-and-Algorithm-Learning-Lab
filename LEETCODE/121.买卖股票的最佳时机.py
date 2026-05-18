class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        def dfs(day, hold, num):
            if num < 0:
                return -float("inf")
            if day < 0:
                return -float("inf") if hold else 0
            if hold:
                return max(dfs(day-1, True, num), dfs(day-1, False, num-1)-prices[day])
            else:
                return max(dfs(day-1, False, num), dfs(day-1, True, num)+prices[day])
        ans = dfs(n-1, False, 1)
        return ans if ans > 0 else 0
    
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dis = [[[-float("inf")]*2 for _ in range(n+1)] for _ in range(3)]
        for num in range(1, 3):
            dis[num][0][0] = 0
        for num in range(1, 3):
            for i in range(n):
                dis[num][i+1][0] = max(dis[num][i][0], dis[num][i][1] + prices[i])
                dis[num][i+1][1] = max(dis[num][i][1], dis[num-1][i][0] - prices[i])
        return dis[-1][-1][0]
    
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))