class Solution:
    def countCompleteComponents(self, n, edges):
        g = [[] for _ in range(n)]
        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
        vis = [0]*n
        
        def dfs(x):
            nonlocal v, e
            vis[x] = 1
            v += 1
            e += len(g[x])
            for y in g[x]:
                if vis[y] == 0:
                    dfs(y)
        
        cnt = 0
        for i in range(n):
            if vis[i] == 0:
                v, e = 0, 0
                dfs(i)
                cnt += 1 if e == v*(v-1) else 0
        return cnt

n = 3
connections = [[1,0],[2,1]]
print(Solution().countCompleteComponents(n, connections))    