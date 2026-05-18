class Solution:
    def minTime(self, n, edges):
        from heapq import heappop, heappush
        g = [[] for _ in range(n)]
        for x, y, start, end in edges:
            g[x].append((y, start, end))
        dis = [float("inf")]*n
        dis[0] = 0
        h = [(0, 0)]

        while h:
            xt, x = heappop(h)
            if xt > dis[x]:
                continue
            for y, start, end in g[x]:
                yt = xt + 1
                if yt > end+1:
                    continue
                elif yt < start+1:
                    yt = start+1
                
                if yt < dis[y]:
                    dis[y] = yt
                    heappush(h, (yt, y))
        return dis[-1] if dis[-1] < float("inf") else -1
    
n = 3
edges = [[0,1,0,1],[1,2,2,5]]
print(Solution().minTime(n, edges))