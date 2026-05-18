#复习：遇到已访问的非父节点，就证明有环
class Solution:
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])
        vis = [[1]*n for _ in range(m)]

        def dfs(pre_i, pre_j, i, j):
            if vis[i][j] == 0:
                return True
            vis[i][j] = 0
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if (x, y) == (pre_i, pre_j):
                    continue
                if 0 <= x < m and 0 <= y < n and grid[x][y] == grid[i][j]:
                    if dfs(i, j, x, y):
                        return True
            return False 

        for i in range(m):
            for j in range(n):
                if vis[i][j] == 1 and dfs(-1, -1, i, j):
                    return True
        return False
    
class Solution1:
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])
        vis = [[1]*n for _ in range(m)]

        def dfs(pre_i, pre_j, i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] != val:
                return False
            if vis[i][j] == 0:
                return True
            vis[i][j] = 0
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if (x, y) == (pre_i, pre_j):
                    continue
                if dfs(i, j, x, y):
                    return True

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if vis[i][j] == 1 and dfs(-1, -1, i, j):
                    return True
        return False

grid = [["f","a","a","c","b"],["e","a","a","e","c"],["c","f","b","b","b"],["c","e","a","b","e"],["f","e","f","b","f"]]
sol = Solution1()
print(sol.containsCycle(grid))