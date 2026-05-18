class Solution:
    def findShortestCycle(self, n, edges):
        from collections import deque
        g = [[] for _ in range(n)]
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)

        ans = n+1
        for i in range(n):
            vis = [-1]*n
            vis[i] = 0
            q = deque([(i, -1)])
            while q:
                x, fa = q.popleft()
                for y in g[x]:
                    if vis[y] < 0:
                        vis[y] = vis[x]+1
                        q.append((y, x))
                    elif y != fa:
                        ans = min(ans, vis[x]+vis[y]+1)
        return ans if ans != n+1 else -1

n = 7
edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
print(Solution().findShortestCycle(n, edges))