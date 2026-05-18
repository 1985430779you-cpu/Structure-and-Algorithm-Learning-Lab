#重点复习:除了坐标，还需要记录蛇的状态
class Solution:
    def minimumMoves(self, grid):
        n = len(grid)
        vis = [[[1]*2 for _ in range(n)] for _ in range(n)]
        vis[0][0][0] = 0
        queue = [(0, 0, 0)]
        cnt = 1

        #(x2, y2) = (x1+s, y1+(s^1))
        while queue:
            tmp = queue
            queue = []
            for X, Y, S in tmp:
                for t in (X + 1, Y, S), (X, Y + 1, S), (X, Y, S ^ 1): 
                    x1, y1, s = t
                    x2, y2 = x1 + s, y1 + (s^1)
                    if x1 < n and y1 < n and x2 < n and y2 < n \
                        and vis[x1][y1][s] != 0 and grid[x1][y1] == 0 and grid[x2][y2] == 0 \
                            and (s == S or grid[x1 + 1][y1 + 1] == 0):
                        if x1 == n-1 and y1== n-2: 
                            return cnt
                        queue.append((x1, y1, s))
                        vis[x1][y1][s] = 0
            cnt += 1
        return -1

grid = [[0,0,0,0,0,1],
        [1,1,0,0,1,0],
        [0,0,0,0,1,1],
        [0,0,1,0,1,0],
        [0,1,1,0,0,0],
        [0,1,1,0,0,0]]
sol = Solution()
print(sol.minimumMoves(grid))  