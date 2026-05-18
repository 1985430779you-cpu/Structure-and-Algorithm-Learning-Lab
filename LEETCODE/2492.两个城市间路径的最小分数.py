class Solution:
    def minScore(self, n, roads):
        from collections import defaultdict
        g = [defaultdict(list) for _ in range(n+1)]
        for road in roads:
            g[road[0]][road[1]] = road[2]
            g[road[1]][road[0]] = road[2]
        vis = [0]*(n+1)
        ans = float("inf")
        path = []

        def dfs(x):
            nonlocal ans
            vis[x] = 1
            for key, value in g[x].items():
                ans = min(ans, value)
                if vis[key] == 0:
                    dfs(key)
            return
        
        dfs(1)
        return ans

n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]
print(Solution().minScore(n, roads))