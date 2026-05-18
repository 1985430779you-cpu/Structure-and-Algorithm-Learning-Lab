class Solution:
    def countPaths(self, n, roads):
        from heapq import heappop, heappush
        from functools import cache
        MOD = 10**9 + 7
        g = [[] for _ in range(n)]
        for x, y, t in roads:
            g[x].append((y, t))
            g[y].append((x, t))
        dis = [float("inf")]*n
        dis[0] = 0
        h = [(0, 0)]

        while h:
            xt, x = heappop(h)
            if xt > dis[x]:
                continue         
            for y, dt in g[x]:
                yt = xt + dt
                if yt < dis[y]:
                    dis[y] = yt
                    heappush(h, (yt, y))
        
        if dis[-1] == float("inf"):
            return 0
        
        @cache
        def dfs(x):
            if x == n-1:
                return 1
            total = 0
            for y, dt in g[x]:
                if dis[x] + dt == dis[y]:
                    total += dfs(y)            
            return total

        return dfs(0) % MOD

n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(Solution().countPaths(n, roads))