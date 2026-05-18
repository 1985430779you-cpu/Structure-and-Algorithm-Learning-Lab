class Solution:
    def findMaxFish(self, grid):
        m, n = len(grid), len(grid[0])
        pos = [[1]*n for _ in range(m)]
        total = []

        def dfs(i, j):
            if (i < 0 or i >= m or j < 0 or j >= n) or (grid[i][j] == 0) or (pos[i][j] == 0):
                return 0         
            pos[i][j] = 0
            sum = int(grid[i][j])
            sum += dfs(i-1,j)
            sum += dfs(i+1,j)
            sum += dfs(i,j-1)
            sum += dfs(i,j+1)
            return sum

        for i in range(m):
            for j in range(n):
                if grid[i][j] >= 1 and pos[i][j] == 1:
                    total.append(dfs(i, j))
        return max(total) if total else 0

grid = [['0','2','1','0'],
        ['4','0','0','3'],
        ['1','0','0','4'],
        ['0','3','2','0']]
sol = Solution()
print(sol.findMaxFish(grid))   