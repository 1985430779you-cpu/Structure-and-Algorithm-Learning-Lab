class Solution:
    def secondMinimum(self, n, edges, time, change):
        from heapq import heappop, heappush
        g = [[] for _ in range(n+1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        dis = [[float("inf"), float("inf")] for _ in range(n+1)]
        dis[1] = [0, float("inf")]
        h = [(0, 1)]
        while h:
            t, x = heappop(h)
            if t > dis[x][1]:
                continue
            for y in g[x]:
                if (t // change) % 2 == 0:
                    yt = t + time
                else:
                    yt = ((t // change) + 1) * change + time
                if yt not in dis[y]:             
                    if yt < dis[y][1]:
                        if yt < dis[y][0]:
                            dis[y][1] = dis[y][0]
                            dis[y][0] = yt
                        else:
                            dis[y][1] = yt
                        heappush(h, (yt, y))
        return dis[n][1]

n = 7
edges = [[1,2],[1,3],[2,5],[2,6],[6,5],[5,7],[3,4],[4,7]]
time = 4
change = 7
print(Solution().secondMinimum(n, edges, time, change))