class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        from heapq import heappop, heappush
        g = [[] for _ in range(n)]
        for x, y, c in flights:
            g[x].append((y, c))
        
        dis = [[float("inf")]*(k+2) for _ in range(n)]
        dis[src][0] = 0
        h = [[0, 0, src]]
        while h:
            cost, transfer, x = heappop(h)
            for y, dc in g[x]:
                new_cost = cost+dc
                new_transfer = transfer+1
                if new_transfer < k+2 and new_cost < dis[y][new_transfer]:
                    dis[y][new_transfer] = new_cost
                    heappush(h, (new_cost, new_transfer, y))
        ans = min(dis[dst])
        return ans if ans < float("inf") else -1

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(Solution().findCheapestPrice(n, flights, src, dst, k))