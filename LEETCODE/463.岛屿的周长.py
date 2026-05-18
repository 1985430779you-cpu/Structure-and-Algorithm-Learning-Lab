class Solution:
    def islandPerimeter(self, grid):
        m, n = len(grid), len(grid[0])
        pos = [[1]*n for _ in range(m)]
        rowpos = [[1]*n for _ in range(m+1)]
        colpos = [[1]*(n+1) for _ in range(m)]
        ans = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0
            if pos[i][j] == 0:
                return 0
            pos[i][j] = 0
            s = 4
            for value in [rowpos[i][j], rowpos[i+1][j], colpos[i][j], colpos[i][j+1]]:
                if value == 0:
                    s -= 2
            rowpos[i][j] = 0
            rowpos[i+1][j] = 0
            colpos[i][j] = 0
            colpos[i][j+1] = 0
            s += dfs(i-1,j)
            s += dfs(i+1,j)
            s += dfs(i,j-1)
            s += dfs(i,j+1)
            return s
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and pos[i][j] == 1:
                    ans = dfs(i, j)
                    break
        return ans
    
class Solution1:
    def islandPerimeter(self, grid):
        m, n = len(grid), len(grid[0])
        pos = [[1]*n for _ in range(m)]
        ans = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if grid[i][j] == 0:
                return 1
            if pos[i][j] == 0:
                return 0
            pos[i][j] = 0
            s = 0
            s += dfs(i-1,j)
            s += dfs(i+1,j)
            s += dfs(i,j-1)
            s += dfs(i,j+1)
            return s
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and pos[i][j] == 1:
                    ans = dfs(i, j)
                    break
        return ans
    
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
sol = Solution()
print(sol.islandPerimeter(grid))   