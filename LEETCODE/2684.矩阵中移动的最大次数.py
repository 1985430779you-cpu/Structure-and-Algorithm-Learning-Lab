class Solution:
    def numEnclaves(self, grid):
        m, n = len(grid), len(grid[0])
        pos = [[1]*n for _ in range(m)]
        ans = []

        from functools import cache
        @cache
        def dfs(i, j, tmp):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] <= tmp:
                return 0
            if pos[i][j] == 0:
                return 0
            tmp = grid[i][j]
            return max(dfs(i-1,j+1,tmp), dfs(i,j+1,tmp), dfs(i+1,j+1,tmp)) + 1
        
        for i in range(m):
            ans.append(dfs(i, 0, 0)-1)
        
        return max(ans) if ans else 0
    
grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
sol = Solution()
print(sol.numEnclaves(grid))