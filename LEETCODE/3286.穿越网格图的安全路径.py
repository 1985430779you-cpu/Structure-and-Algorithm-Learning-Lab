class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])
        vis = [[[1]*(health+1) for _ in range(n)] for _ in range(m)]
        if health - grid[0][0] >= 1:
            q = [(0, 0, health - grid[0][0])]
            vis[0][0][health] = 0
        else:
            return False
        ans = False

        while q:
            tmp = q
            q = []
            for X, Y, H in tmp:
                for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                    x, y = X+dx, Y+dy
                    if 0 <= x < m and 0 <= y < n:
                        health = H - grid[x][y]
                        if x == m-1 and y == n-1 and health >= 1:
                            ans = True
                        if health >= 1:
                            if vis[x][y][health] == 1:
                                q.append((x, y, health))
                                vis[x][y][health] = 0
            if ans:
                return True       
        return False
    
grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
health = 1
print(Solution().findSafeWalk(grid, health))