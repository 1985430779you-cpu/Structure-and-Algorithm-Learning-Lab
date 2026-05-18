class Solution:
    def swimInWater(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if vis[i][j] == 0:
                return False
            vis[i][j] = 0
            if i == m-1 and j == n-1:
                return True
            for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
                x, y = i+di, j+dj
                if 0 <= x < m and 0 <= y < n and mid >= grid[x][y]:
                    if dfs(x, y):
                        return True
            return False
        
        mx = max([max(row) for row in grid])
        low, high = 0, mx
        while low <= high:
            mid = (low+high) // 2
            vis = [[1]*n for _ in range(m)]
            if grid[0][0] > mid:
                low = mid+1
                continue
            if dfs(0, 0):
                high = mid-1
            else:
                low = mid+1
        
        return low
    
class Solution1:
    def swimInWater(self, grid):
        from heapq import heappop, heappush
        m, n = len(grid), len(grid[0])
        dis = [[float("inf")]*n for _ in range(m)]
        dis[0][0] = grid[0][0]
        h = [(grid[0][0], 0, 0)]
        while h:
            t, x, y = heappop(h)
            if t > dis[x][y]:
                continue
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                X, Y = x+dx, y+dy
                if 0 <= X < n and 0 <= Y < m:
                    if t < grid[X][Y]:
                            T = grid[X][Y]
                    else:
                         T = t
                    if T < dis[X][Y]:
                         dis[X][Y] = T
                         heappush(h, (T, X, Y))
        return dis[-1][-1]

    
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(Solution1().swimInWater(grid))      