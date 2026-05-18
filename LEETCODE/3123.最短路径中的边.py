class Solution:
    def findAnswer(self, n, edges):
        from heapq import heappop, heappush
        from collections import deque
        g = [[] for _ in range(n)]
        for i, (x, y, c) in enumerate(edges):
            g[x].append((y, c, i))
            g[y].append((x, c, i))
        dis = [float("inf")]*n
        dis[0] = 0
        h = [(0, 0)]

        while h:
            xc, x = heappop(h)
            if xc > dis[x]:
                continue         
            for y, dc, _ in g[x]:
                yc = xc + dc
                if yc < dis[y]:
                    dis[y] = yc
                    heappush(h, (yc, y))

        ans = [False]*len(edges)
        if dis[-1] == float("inf"):
            return ans
        
        queue = deque([n-1])
        vis = [False] * n
        vis[n-1] = True
        
        while queue:
            x = queue.popleft()            
            for y, c, i in g[x]:
                # 检查是否满足最短路径条件：dist[v] + w == dist[u]
                if dis[y] + c == dis[x]:
                    ans[i] = True
                    if not vis[y]:
                        vis[y] = True
                        queue.append(y)
        return ans

n = 6
edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]
print(Solution().findAnswer(n, edges))          