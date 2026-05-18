#重点复习:除了坐标，还需要记录k
class Solution:
    def shortestPath(self, grid, k):
        from collections import deque
        m, n = len(grid), len(grid[0])
        #k的情况也需要记录
        vis = [[[1]*(k+1) for _ in range(n)] for _ in range(m)]
        queue = deque([(0, 0, k, 0)])
        vis[0][0][k] = 0
        if 0 == m-1 and 0 == n-1:
            return 0

        while queue: 
            a, b, c, step = queue.popleft()
            if a == m-1 and b == n-1:
                return step
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                x, y = a+dx, b+dy
                if 0 <= x < m and 0 <= y < n:
                    new_c = c - grid[x][y]
                    if vis[x][y][new_c] != 0 and new_c >= 0:
                        vis[x][y][new_c] = 0
                        queue.append((x, y, new_c, step+1))
        return -1         
    
grid = [[0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,1,1],
        [0,1,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,1,1],
        [0,1,0,1,1,1,1,0,0,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,0,1,0]]
k = 1
print(Solution().shortestPath(grid, k))    