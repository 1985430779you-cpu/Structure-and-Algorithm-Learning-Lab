class Solution:
    def highestRankedKItems(self, grid, pricing, start, k):
        from collections import deque
        m, n = len(grid), len(grid[0])
        vis = [[1]*n for _ in range(m)]
        queue = deque([(start[0], start[1])])
        vis[start[0]][start[1]] = 0
        low, high = pricing[0], pricing[1]
        treasure = [(0, grid[start[0]][start[1]], start[0], start[1])] if low <= grid[start[0]][start[1]] <= high else []
        ans = []
        cnt = 0

        while queue:
            length = len(queue)
            for _ in range(length):
                a, b = queue.popleft()
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    x, y = a+dx, b+dy
                    if 0 <= x < m and 0 <= y < n and vis[x][y] != 0 and grid[x][y] != 0:
                        queue.append((x, y))
                        vis[x][y] = 0
                        if low <= grid[x][y] <= high:
                            treasure.append((cnt+1, grid[x][y], x, y))
            cnt += 1

        treasure.sort()
        for _, _, i, j in treasure[:k]:
            ans.append([i, j]) 
        return ans

grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]]
pricing = [2,3] 
start = [2,3]
k = 2
print(Solution().highestRankedKItems(grid, pricing, start, k))  