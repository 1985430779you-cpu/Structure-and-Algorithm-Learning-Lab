class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        g = [[] for _ in range(n)]
        for i in range(n-1):
            g[i].append(i+1)
        
        ans = []
        for a, b in queries:
            g[a].append(b)
            vis = [-1]*n
            vis[0] = 0
            q = [0]
            while q:
                x = q.pop(0)
                for y in g[x]:
                    if vis[y] < 0:
                        vis[y] = vis[x] + 1
                        q.append(y)
            ans.append(vis[-1])
        return ans
    
n = 5
queries = [[2, 4], [0, 2], [0, 4]]
print(Solution().shortestDistanceAfterQueries(n, queries))