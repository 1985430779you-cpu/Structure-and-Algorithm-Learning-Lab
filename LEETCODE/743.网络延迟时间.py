class Solution:
    def networkDelayTime(self, times, n, k):
        import heapq
        g = [[] for _ in range(n+1)]
        for x, y, t in times:
            g[x].append((y, t))

        dis = [float("inf")]*(n+1)
        dis[k] = 0
        h = [(0, k)]
        while h:
            dis_x, x = heapq.heappop(h)
            if dis_x > dis[x]:
                continue
            for y, t in g[x]:
                dis_y = dis_x + t
                if dis_y < dis[y]:
                    dis[y] = dis_y
                    heapq.heappush(h, (dis[y], y))
        return max(dis[1:]) if max(dis[1:]) < float("inf") else -1
    
times = [[1,2,1],[2,1,3]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n, k))