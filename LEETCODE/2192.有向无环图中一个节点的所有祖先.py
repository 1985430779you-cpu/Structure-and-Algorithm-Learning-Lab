class Solution:
    def getAncestors(self, n, edges):
        g = [[] for _ in range(n)]
        ans = [[] for _ in range(n)]
        for edge in edges:
            g[edge[1]].append(edge[0])
    
        def dfs(x):
            vis[x] = 1
            for y in g[x]:
                if vis[y] == 0:
                    dfs(y)
        
        for i in range(n):
            vis = [0]*n
            dfs(i)
            vis[i] = 0
            for j in range(n):
                if vis[j] == 1:
                    ans[i].append(j)
        return ans
    
n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
print(Solution().getAncestors(n, edgeList))    