class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        g = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    g[i].append(j)
        vis = [0] * n
        
        def dfs(x):
            vis[x] = 1
            for y in g[x]:
                if vis[y] == 0:
                    dfs(y)
        
        cnt = 0
        for i in range(n):
            if vis[i] == 0:
                dfs(i)
                cnt += 1
        
        return cnt

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))    