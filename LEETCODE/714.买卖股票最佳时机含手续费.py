class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        dis = [[0]*2 for _ in range(n+1)]
        dis[0][0] = 0
        dis[0][1] = -float("inf")

        for i in range(n):
            dis[i+1][0] = max(dis[i][0], dis[i][1]+prices[i])
            dis[i+1][1] = max(dis[i][1], dis[i][0]-prices[i]-fee)
        return dis[-1][0]

prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(Solution().maxProfit(prices, fee))