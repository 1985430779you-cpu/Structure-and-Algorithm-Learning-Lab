class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True
        pos = [[1]*n for _ in range(m)]
        pos[0][0] = 0
        hash = {1:[(0, 1), (0, -1)], 2:[(1, 0), (-1, 0)], 3:[(1, 0), (0, -1)],
                4:[(0, 1), (1, 0)], 5:[(-1, 0), (0, -1)], 6:[(-1, 0), (0, 1)]}
        
        def dfs(i, j, tmp):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if pos[i][j] == 0:
                return False
            if all([i+x, j+y] != tmp for x, y in hash[grid[i][j]]):
                return False 
            if i == m-1 and j == n-1:
                return True
            pos[i][j] = 0
            tmp = [i, j]
            for x, y in hash[grid[i][j]]:
                if dfs(i+x, j+y, tmp):
                    return True
            return False

        for x, y in hash[grid[0][0]]:
            if dfs(x, y, [0, 0]):
                return True
        return False
    
grid = [[2,4,3],[6,5,2]]
sol = Solution()
print(sol.hasValidPath(grid))