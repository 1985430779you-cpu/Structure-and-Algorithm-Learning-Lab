class Solution:
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])
        pos = [[1]*n for _ in range(m)]
        cnt = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if grid[i][j] == 1:
                return 0
            if pos[i][j] == 0:
                return 0
            pos[i][j] = 0
            return max(dfs(i+1,j), dfs(i-1,j), dfs(i,j+1), dfs(i,j-1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and pos[i][j] == 1:
                    s = dfs(i, j)
                    if s == 0:
                        cnt += 1
        return cnt
    
grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]
sol = Solution()
print(sol.closedIsland(grid))