class Solution:
    def minCost(self, n, edges):
        from heapq import heappop, heappush
        g = [[] for _ in range(n)]
        r_g = [[] for _ in range(n)]
        for x, y, c in edges:
            g[x].append((y, c))
            r_g[y].append((x, 2*c))
        dis = [float("inf")]*n
        dis[0] = 0
        h = [(0, 0)]        
        
        while h:
            xc, x = heappop(h)
            if xc > dis[x]:
                continue
            for y, dc in r_g[x]:
                yc = xc + dc
                if yc < dis[y]:
                    dis[y] = yc
                    heappush(h, (yc, y))            
            for y, dc in g[x]:
                yc = xc + dc
                if yc < dis[y]:
                    dis[y] = yc
                    heappush(h, (yc, y))
        return dis[-1] if dis[-1] < float("inf") else -1

n = 3
edges = [[2,1,1],[1,0,1],[2,0,16]]
print(Solution().minCost(n, edges))                