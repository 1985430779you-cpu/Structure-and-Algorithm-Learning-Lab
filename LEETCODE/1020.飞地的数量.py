class Solution:
    def numEnclaves(self, grid):
        m, n = len(grid), len(grid[0])
        pos = [[1]*n for _ in range(m)]
        ans = []

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return float("-inf")
            if grid[i][j] == 0:
                return 0
            if pos[i][j] == 0:
                return 0
            pos[i][j] = 0
            s = 1
            s += dfs(i-1,j)
            s += dfs(i+1,j)
            s += dfs(i,j-1)
            s += dfs(i,j+1)
            return s
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and pos[i][j] == 1:
                    s = dfs(i, j)
                    if s > 0:
                        ans.append(s)
        return sum(ans) if ans else 0
    
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
sol = Solution()
print(sol.numEnclaves(grid))