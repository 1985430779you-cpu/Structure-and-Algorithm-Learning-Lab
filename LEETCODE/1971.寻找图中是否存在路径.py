class Solution:
    def validPath(self, n, edges, source, destination):
        g = [[] for _ in range(n)]
        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
        vis = [0]*n
        if source == destination:
            return True

        def dfs(x):
            if x == destination:
                return True
            vis[x] = 1
            for y in g[x]:
                if vis[y] == 0:
                    if dfs(y):
                        return True
            return False

        return dfs(source)
    
n = 3
edges= [[0,1],[1,2],[2,0]]
source = 0
destination = 2
print(Solution().validPath(n, edges, source, destination))    