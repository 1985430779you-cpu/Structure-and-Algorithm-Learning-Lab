class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        pos = [[1]*n for _ in range(m)]
        count = 0
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] == "0":
                return
            if pos[i][j] == 0:
                return
            pos[i][j] = 0
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and pos[i][j] == 1:
                    dfs(i, j)
                    count += 1
        return count

grid = [['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0']]
sol = Solution()
print(sol.numIslands(grid))        