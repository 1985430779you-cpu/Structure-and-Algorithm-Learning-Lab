#套路题
class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        
        def dfs(i, j):
            if vis[i][j] == 0:
                return False
            vis[i][j] = 0
            if i == m-1 and j == n-1:
                return True
            for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
                x, y = i+di, j+dj
                if 0 <= x < m and 0 <= y < n and abs(heights[i][j]-heights[x][y]) <= mid:
                    if dfs(x, y):
                        return True
            return False

        mx = max([max(row) for row in heights])
        low, high = 0, mx
        while low <= high:
            vis = [[1]*n for _ in range(m)]
            mid = (low+high) // 2
            if dfs(0,0):
                high = mid - 1
            else:
                low = mid + 1
        return low

class Solution1:
    def minimumEffortPath(self, heights):
        from heapq import heappop, heappush
        m, n = len(heights), len(heights[0])
        dis = [[float("inf")]*n for _ in range(m)]
        dis[0][0] = 0
        h = [(0, 0, 0)]

        while h:
            c, x, y = heappop(h)
            if c > dis[x][y]:
                continue
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                X, Y = x+dx, y+dy
                if 0 <= X < m and 0 <= Y < n:
                    C = abs(heights[X][Y] - heights[x][y])
                    C = max(C, c)
                    if C < dis[X][Y]:
                        dis[X][Y] = C
                        heappush(h, (C, X, Y))
        return dis[-1][-1]

heights = [[3]]
print(Solution1().minimumEffortPath(heights))        