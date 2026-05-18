class Solution:
    def shortestBridge(self, grid):
        from collections import deque
        n = len(grid)
        vis = [[1]*n for _ in range(n)]
        queue = deque([])
        cnt = 0
        tmpi = tmpj = -1
        Find = False

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    tmpi, tmpj = i, j
                    break
            if tmpi != -1:
                break

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= n:
                return
            if grid[i][j] != 1:
                return
            if vis[i][j] == 0:
                return
            vis[i][j] = 0
            queue.append((i,j))
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                dfs(i+dx, j+dy)
        dfs(tmpi, tmpj)

        while queue:
            length = len(queue)
            for _ in range(length):
                a, b = queue.popleft()
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    x, y = a+dx, b+dy
                    if 0 <= x < n and 0 <= y < n and vis[x][y] != 0:
                        if grid[x][y] == 1:
                            Find = True
                            break
                        queue.append([x,y])
                        vis[x][y] = 0
            if Find:
                return cnt
            else:
                cnt += 1

grid = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]
sol = Solution()
print(sol.shortestBridge(grid))    