class Solution:
    def largestArea(self, grid):
        m, n = len(grid), len(grid[0])
        pos = [[1]*n for _ in range(m)]
        ans = []

        import math
        def dfs(i, j, val):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] == "0":
                return -math.inf
            if grid[i][j] != val or pos[i][j] == 0:
                return 0
            pos[i][j] = 0
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                return -math.inf
            s = 1
            s += dfs(i-1,j,val)
            s += dfs(i+1,j,val)
            s += dfs(i,j-1,val)
            s += dfs(i,j+1,val)
            return s

        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] > "0" and pos[i][j] == 1:
                    a = dfs(i, j, grid[i][j])
                    if a > 0:
                        ans.append(a)
        if not ans:
            return 0
        return max(ans)
    
grid = ["000","010","000"]
sol = Solution()
print(sol.largestArea(grid))   