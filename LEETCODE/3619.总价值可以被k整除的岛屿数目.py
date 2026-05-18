class Solution:
    def countIslands(self, grid, k):
        m, n = len(grid), len(grid[0])
        pos = [[1]*(n) for _ in range(m)]
        ans, cnt = [], 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0
            if pos[i][j] == 0:
                return 0
            pos[i][j] = 0
            s = grid[i][j]
            s += dfs(i+1, j)
            s += dfs(i-1, j)
            s += dfs(i, j+1)
            s += dfs(i, j-1)
            return s
        
        for i in range(m):
            for j in range(n):
                if pos[i][j] == 1 and grid[i][j] > 0:
                    ans.append(dfs(i, j))
        if not ans:
            return 0
        for value in ans:
            if value % k == 0:
                cnt += 1
        return cnt
    
grid = [[0,2,1,0,0],
        [0,5,0,0,5],
        [0,0,1,0,0],
        [0,1,4,7,0],
        [0,2,0,0,8]]
k = 5
sol = Solution()
print(sol.countIslands(grid, k))     