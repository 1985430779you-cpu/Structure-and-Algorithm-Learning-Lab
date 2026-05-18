#暴力解法
class Solution:
    def minMalwareSpread(self, graph, initial):
        n = len(graph)
        initial.sort()
        ans = n
        ans_x = n

        def dfs(x):
            vis[x] = 1
            s = 1
            for y in g[x]:
                if vis[y] == 0:
                    s += dfs(y)
            return s

        for k in initial:
            g = [[] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i != k and j != k:
                        if graph[i][j] == 1:
                            g[i].append(j)

            vis = [0]*n
            s = 0
            for l in initial:
                if l == k:
                    continue
                if vis[l] == 0:
                    s += dfs(l)
            if s < ans:                    
                ans = s
                ans_x = k
        
        return ans_x
        
graph = [[1,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0],[0,0,1,0,1,0,1,0,0],[0,0,0,1,0,0,0,0,0],[0,0,1,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,1]]
initial = [6,0,4]
print(Solution().minMalwareSpread(graph, initial))    