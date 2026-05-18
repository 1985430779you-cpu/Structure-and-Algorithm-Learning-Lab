class Solution:
    def minTimeToReach(self, moveTime):
        from heapq import heappop, heappush
        n, m = len(moveTime), len(moveTime[0])
        dis = [[float("inf")]*m for _ in range(n)]
        dis[0][0] = 0
        h = [(0, 0, 0, 0)]
        while h:
            t, x, y, s = heappop(h)
            if t > dis[x][y]:
                continue
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                X, Y = x+dx, y+dy
                if 0 <= X < n and 0 <= Y < m:
                    if t < moveTime[X][Y]:
                            T = moveTime[X][Y]+(s+1)
                    else:
                         T = t+(s+1)
                    if T < dis[X][Y]:
                        dis[X][Y] = T
                        heappush(h, (T, X, Y, s^1))
        return dis[-1][-1]
    
moveTime = [[0,4],[4,4]]
print(Solution().minTimeToReach(moveTime))        