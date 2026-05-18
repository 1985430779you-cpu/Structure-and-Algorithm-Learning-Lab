class Solution:
    def colorBorder(self, grid, row, col, color):
        m, n = len(grid), len(grid[0])
        pos = [[1]*n for _ in range(m)]
        val = grid[row][col]
        
        def dfs(i, j): #顺序很重要：先检查越界，再看有没来过，最后对比值
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if pos[i][j] == 0:
                return 0
            if grid[i][j] != val:
                return 1
            pos[i][j] = 0
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if dfs(x, y) == 1:
                    grid[i][j] = color
            return
        dfs(row, col)
        return grid