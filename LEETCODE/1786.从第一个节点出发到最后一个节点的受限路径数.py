class Solution:
    def countRestrictedPaths(self, n, edges):
        MOD = 10**9 + 7
        from heapq import heappop, heappush
        from functools import cache
        g = [[] for _ in range(n)]
        for x, y, c in edges:
            g[x-1].append((y-1, c))
            g[y-1].append((x-1, c))
        dis = [float("inf")]*(n)
        dis[n-1] = 0
        h = [(0, n-1)] 

        while h:
            xc, x = heappop(h)
            if xc > dis[x]:
                continue         
            for y, dc in g[x]:
                yc = xc + dc
                if yc < dis[y]:
                    dis[y] = yc
                    heappush(h, (yc, y))
        
        @cache
        def dfs(x):
            if x == n-1:
                return 1
            total = 0
            for y, _ in g[x]:
                if dis[x] > dis[y]:
                    total += dfs(y)
            return total
        return dfs(0) % MOD

n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
print(Solution().countRestrictedPaths(n, edges))  