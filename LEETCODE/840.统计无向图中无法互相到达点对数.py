class Solution:
    def countPairs(self, n, edges):
        g = [[] for _ in range(n)]
        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
        vis = [0]*n
        path = []
        ans = 0

        def dfs(x):
            vis[x] = 1
            s = 1
            for y in g[x]:
                if vis[y] == 0:
                    s += dfs(y)
            return s

        for i in range(n):
            if vis[i] == 0:
                path.append(dfs(i))
        
        if path:
            s = sum(path)
            for j in range(0, len(path)-1):
                s -= path[j]
                ans += s*path[j]
        return ans
    
n = 7
edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
print(Solution().countPairs(n, edges))    