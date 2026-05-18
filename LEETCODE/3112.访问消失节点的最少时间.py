class Solution:
    def minimumTime(self, n, edges, disappear):
        import heapq
        g = [[] for _ in range(n)]
        for x, y, t in edges:
            g[x].append((y, t))
            g[y].append((x, t))

        dis = [-1]*n
        dis[0] = 0
        h = [(0, 0)]

        while h:
            xt, x = heapq.heappop(h)
            if xt > dis[x]:
                continue
            for y, dt in g[x]:
                yt = xt + dt
                if yt < disappear[y] and (dis[y] == -1 or yt < dis[y]):
                    dis[y] = yt
                    heapq.heappush(h, (yt, y))        
        return dis 
    
n = 2 
edges = [[0,1,1]]
disappear = [1,1,5]
print(Solution().minimumTime(n, edges, disappear))