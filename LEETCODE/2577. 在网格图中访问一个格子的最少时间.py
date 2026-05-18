#迈出第一步一定能到终点
class Solution:
    def minimumTime(self, grid):
        from heapq import heappop, heappush
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        dis = [[float("inf")]*n for _ in range(m)]
        dis[0][0] = 0
        h = [(0, 0, 0)]
        while h:
            t, x, y = heappop(h)
            if t > dis[x][y]:
                continue
            if x == m-1 and y == n-1:
                return t
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                X, Y = x+dx, y+dy
                if 0 <= X < m and 0 <= Y < n:
                    T = max(t+1, grid[X][Y])
                    T += (T-X-Y) % 2
                    if T < dis[X][Y]:
                        dis[X][Y] = T
                        heappush(h, (T, X, Y))
    
grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
print(Solution().minimumTime(grid))