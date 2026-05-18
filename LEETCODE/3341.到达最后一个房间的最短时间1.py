class Solution:
    def minTimeToReach(self, moveTime):
        import heapq
        n, m = len(moveTime), len(moveTime[0])
        dis = [[float("inf")]*m for _ in range(n)]
        dis[0][0] = 0
        h = [(0, 0, 0)]
        while h:
            t, x, y = heapq.heappop(h)
            if t > dis[x][y]:
                continue
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                X, Y = x+dx, y+dy
                if 0 <= X < n and 0 <= Y < m:
                    if t < moveTime[X][Y]:
                            T = moveTime[X][Y] + 1
                    else:
                         T = t+1
                    if T < dis[X][Y]:
                         dis[X][Y] = T
                         heapq.heappush(h, (T, X, Y))
        return dis[-1][-1]
    
moveTime = [[0,1],[1,2]]
print(Solution().minTimeToReach(moveTime))