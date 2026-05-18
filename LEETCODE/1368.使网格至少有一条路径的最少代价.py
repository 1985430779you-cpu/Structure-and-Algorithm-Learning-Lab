class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        ans = [[float("inf")]*n for _ in range(m)]
        hash_dir = {1:(0, 1), 2:(0, -1), 3:(1, 0), 4:(-1, 0)}
        from collections import deque
        q = deque([(0, 0)])
        ans[0][0] = 0

        while q:
            i, j = q.popleft()
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < m and 0 <= y < n:
                    k = 0
                    if (x-i, y-j) != hash_dir[grid[i][j]]:
                        k = 1
                    if ans[i][j] + k < ans[x][y]:
                        ans[x][y] = ans[i][j] + k
                        if k == 0:
                            q.appendleft((x, y))
                        elif k == 1:
                            q.append((x, y))
        return ans[m-1][n-1]   

grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
print(Solution().minCost(grid))       