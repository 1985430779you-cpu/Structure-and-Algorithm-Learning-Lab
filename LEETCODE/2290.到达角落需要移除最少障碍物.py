class Solution0:
    def minimumObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        bur = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bur += 1
        vis = [[[0]*(bur+1) for _ in range(n)] for _ in range(m)]
        
        q = [(0, 0, 0)]
        ans = bur
        while q:
            tmp = q
            q = []
            for X, Y, B in tmp:
                if X == m-1 and Y == n-1:
                    ans = min(ans, B)
                    continue
                for dX, dY in (1, 0), (-1, 0), (0, 1), (0, -1):
                    x, y = X+dX, Y+dY
                    if 0 <= x < m and 0 <= y < n:
                        b = B+grid[x][y]
                        if b <= bur and vis[x][y][b] == 0:
                            q.append((x, y, b))
                            vis[x][y][b] = 1
        
        return ans
    
class Solution:
    def minimumObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        ans = [[float("inf")]*n for _ in range(m)]
        from collections import deque
        q = deque([(0, 0)])
        ans[0][0] = 0

        while q:
            i, j = q.popleft()
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < m and 0 <= y < n:
                    if ans[i][j] + grid[x][y] < ans[x][y]:
                        ans[x][y] = ans[i][j] + grid[x][y]
                        if grid[x][y] == 0:
                            q.appendleft((x, y))
                        else:
                            q.append((x, y))
        return ans[m-1][n-1]
    
grid = [[0,1,1],[1,1,0],[1,1,0]]
print(Solution().minimumObstacles(grid))  