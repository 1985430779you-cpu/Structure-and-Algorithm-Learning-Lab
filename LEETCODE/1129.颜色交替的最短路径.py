class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        from collections import deque
        red_g = [[] for _ in range(n)]
        blue_g = [[] for _ in range(n)]
        for i, j in redEdges:
            red_g[i].append(j)
        for x, y in blueEdges:
            blue_g[x].append(y)
        
        ans = [-1]*n
        for start in 0, 1:
            vis = [[float("inf")]*n for _ in range(2)]
            vis[start][0] = 0
            q = deque([(0, start)])
            while q:
                x = q.popleft()
                if x[1] == 0:
                    color_g = red_g
                elif x[1] == 1:
                    color_g = blue_g
                for y in color_g[x[0]]:
                    if vis[x[1]^1][y] == float("inf"):
                        vis[x[1]^1][y] = vis[x[1]][x[0]]+1
                        q.append((y, x[1]^1))
    
            for i in range(len(ans)):
                if vis[0][i] != float("inf") or vis[1][i] != float("inf"):
                    if ans[i] == -1:
                        ans[i] = min(vis[0][i], vis[1][i])
                    else:
                        ans[i] = min(vis[0][i], vis[1][i], ans[i])
        return ans

n = 5
redEdges = [[0,1],[1,2],[2,3],[3,4]]
blueEdges = [[1,2],[2,3],[3,1]]
print(Solution().shortestAlternatingPaths(n, redEdges, blueEdges))