class Solution:
    def updateMatrix(self, mat):
        from collections import deque
        m, n = len(mat), len(mat[0])
        vis = [[1]*n for _ in range(m)]
        queue = deque([])
        cnt = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    vis[i][j] = 0
        
        while queue:
            length = len(queue)
            for _ in range(length):
                a, b = queue.popleft()
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    x, y = a+dx, b+dy
                    if 0 <= x < m and 0 <= y < n and vis[x][y] != 0 and mat[x][y] != 0:
                        queue.append((x, y))
                        vis[x][y] = 0
            cnt += 1
            if not queue:
                break
            for i, j in queue:
                mat[i][j] = cnt
        return mat
    
grid = [[0,0,0],[0,1,0],[1,1,1]]
sol = Solution()
print(sol.updateMatrix(grid))    