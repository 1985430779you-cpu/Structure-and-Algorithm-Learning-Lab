#记忆化+dfs以减少时间复杂度
class Solution:
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        ans = 1

        from functools import cache
        @cache
        def dfs(i, j):
            mx = 1
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < m and 0 <= y < n and matrix[i][j] < matrix[x][y]:
                    mx = max(mx, dfs(x, y) + 1)
            return mx
        
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans
    
matrix = [[7,6,1,1],[2,7,6,0],[1,3,5,1],[6,6,3,2]]
print(Solution().longestIncreasingPath(matrix))  