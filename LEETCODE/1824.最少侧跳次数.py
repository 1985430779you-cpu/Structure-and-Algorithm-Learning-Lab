class Solution:
    def minSideJumps(self, obstacles):
        from collections import deque
        n = len(obstacles)
        grid = [[0]*n for _ in range(3)]
        ans = [[float("inf")]*n for _ in range(3)]
        for i in range(n):
            if obstacles[i] != 0:
                grid[obstacles[i]-1][i] = 1
        ans[1][0] = 0
        q = deque([(1, 0)])

        while q:
            i, j = q.popleft()
            if j == n-1:
                return ans[i][j]
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                x, y = i+dx, j+dy
                if 0 <= x < 3 and 0 <= y < n:
                    if grid[x][y] == 0 and ((dx, dy) == (0, 1) or (dx, dy) == (0, -1)):
                        if ans[i][j] < ans[x][y]:
                            ans[x][y] = ans[i][j]
                            q.appendleft((x, y))
                    elif grid[x][y] == 0 and ((dx, dy) == (1, 0) or (dx, dy) == (-1, 0)):
                        if ans[i][j] + 1 < ans[x][y]:
                            ans[x][y] = ans[i][j] + 1
                            q.append((x, y))
                    elif grid[x][y] == 1 and ((dx, dy) == (1, 0) or (dx, dy) == (-1, 0)):
                        if ans[i][j] + 1 < ans[x][y]:
                            ans[x][y] = ans[i][j] + 1
                            if 0 <= x+dx < 3 and 0 <= y+dy < n:
                                ans[x+dx][y+dy] = ans[x][y]
                                q.append((x+dx, y+dy))

obstacles = [0,2,1,0,3,0]
print(Solution().minSideJumps(obstacles))