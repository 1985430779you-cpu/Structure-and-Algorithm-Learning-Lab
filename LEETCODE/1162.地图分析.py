class Solution:
    def maxDistance(self, grid):
        from collections import deque
        n = len(grid)
        vis = [[1]*n for _ in range(n)]
        queue = deque([])
        cnt = -1       
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j])
                    vis[i][j] = 0
        if not queue or len(queue) == n**2:            
            return -1
        while queue:
            length = len(queue)
            for _ in range(length):
                a = queue.popleft()
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    x, y = a[0]+dx, a[1]+dy
                    if 0 <= x < n and 0 <= y < n and vis[x][y] != 0:
                        queue.append([x,y])
                        vis[x][y] = 0
            cnt += 1                        
        return cnt
    
grid = [[1,0,1],[0,0,0],[1,0,1]]
sol = Solution()
print(sol.maxDistance(grid))    