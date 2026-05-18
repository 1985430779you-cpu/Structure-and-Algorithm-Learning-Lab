class Solution:
    def shortestPathBinaryMatrix(self, grid):
        from collections import deque
        if grid[0][0] != 0:
            return -1
        n = len(grid)
        queue = deque([[0, 0]])
        vis = [[1]*n for _ in range(n)]
        vis[0][0] = 0
        cnt = 1
        Find = False
        if n-1 == 0:
            return cnt

        while queue:
            length = len(queue)
            for _ in range(length):
                a = queue.popleft()
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1):
                    x, y = a[0]+dx, a[1]+dy
                    if 0 <= x < n and 0 <= y < n and vis[x][y] != 0 and grid[x][y] == 0:
                        if x == n-1 and y == n-1:
                            Find = True
                            break
                        queue.append([x,y])
                        vis[x][y] = 0
            cnt += 1
            if Find:
                return cnt
        return -1 

grid = [[0,1],[1,0]]
sol = Solution()
print(sol.shortestPathBinaryMatrix(grid))    