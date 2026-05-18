class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        vis = [[1]*n for _ in range(n)]
        queue = []
        cnt = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = 0
                    vis[i][j] = 0
                else:
                    grid[i][j] = 1
        
        while queue:
            tmp = queue
            queue = []
            for X, Y in tmp:
                for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                    x, y = X+dx, Y+dy
                    if 0 <= x < n and 0 <= y < n and vis[x][y] != 0:
                        queue.append((x, y))
                        grid[x][y] = cnt
                        vis[x][y] = 0
            cnt += 1
        #return grid

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= n:
                return False
            if vis[i][j] == 0:
                return False
            vis[i][j] = 0
            if grid[i][j] < mid:
                return False
            if i == n-1 and j == n-1:
                return True
            return dfs(i+1, j) or dfs(i-1, j) or dfs(i, j+1) or dfs(i, j-1)

        mx = 0
        for row in grid:
            mx = max(mx, max(row))
        low, high = 0, mx
        while low <= high:
            mid = (low+high) // 2
            vis = [[1]*n for _ in range(n)]
            if dfs(0, 0):
                low = mid+1
            else:
                high = mid-1
        return low-1
    
grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
print(Solution().maximumSafenessFactor(grid))