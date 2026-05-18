class Solution:
    def minimumPath(self, grid):
        m, n = len(grid), len(grid[0])
        record = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                record[i][j] = grid[i][j]
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    record[i][j] += record[i][j-1]
                elif j == 0:
                    record[i][j] += record[i-1][j]
                else:
                    record[i][j] += min(record[i-1][j], record[i][j-1])
        return record[-1][-1]

grid =[[1,2,3],[4,5,6]]
sol = Solution()
print(sol.minimumPath(grid))