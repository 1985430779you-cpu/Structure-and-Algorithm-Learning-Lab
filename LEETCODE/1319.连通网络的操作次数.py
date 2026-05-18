class Solution:
    def makeConnected(self, n, connections):
        m = len(connections)
        if m < n-1:
            return -1
        g = [[] for _ in range(n)]
        for connection in connections:
            g[connection[0]].append(connection[1])
            g[connection[1]].append(connection[0])
        vis = [0]*n

        def dfs(x):
            vis[x] = 1
            for y in g[x]:
                if vis[y] == 0:
                    dfs(y)
        
        ans = -1
        for i in range(n):
            if vis[i] == 0:
                dfs(i)
                ans += 1
        return ans
    
n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
print(Solution().makeConnected(n, connections))    