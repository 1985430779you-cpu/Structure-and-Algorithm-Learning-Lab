class Solution:
    def orangesRotting(self, grid):
        from collections import deque
        m, n = len(grid), len(grid[0])
        vis = [[1]*n for _ in range(m)]
        queue = deque([])
        fresh_orange = 0
        time = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    vis[i][j] = 0
                elif grid[i][j] == 1:
                    fresh_orange += 1
        
        if fresh_orange == 0:
            return 0
        if not queue:
            return -1
        while queue:
            length = len(queue)
            for _ in range(length):
                a, b = queue.popleft()
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    x, y = a+dx, b+dy
                    if 0 <= x < m and 0 <= y < n and vis[x][y] != 0 and grid[x][y] == 1:
                        queue.append((x, y))
                        vis[x][y] = 0
                        fresh_orange -= 1
            time += 1
        
        if fresh_orange > 0:
            return -1
        return time-1
    
grid = [[0,2]]
sol = Solution()
print(sol.orangesRotting(grid))    