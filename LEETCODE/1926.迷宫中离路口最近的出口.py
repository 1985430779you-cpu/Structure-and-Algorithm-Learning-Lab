class Solution:
    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])
        vis = [[1]*n for _ in range(m)]
        queue = [entrance]
        vis[entrance[0]][entrance[1]] = 0
        cnt = 0
        Find = False

        while queue:
            length = len(queue)
            for _ in range(length):
                a = queue.pop(0)
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    x, y = a[0]+dx, a[1]+dy
                    if 0 <= x < m and 0 <= y < n and vis[x][y] != 0 and maze[x][y] != "+":
                        if x == 0 or x == m-1 or y == 0 or y == n-1:
                            Find = True
                            break
                        queue.append([x,y])
                        vis[x][y] = 0
            cnt += 1
            if Find:
                return cnt
        return -1   

maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [0,0]
sol = Solution()
print(sol.nearestExit(maze, entrance))    