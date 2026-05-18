class Solution:
    def conveyorBelt(self, matrix, start, end):
        m, n = len(matrix), len(matrix[0])
        ans = [[float("inf")]*n for _ in range(m)]
        hash_dir = {">":(0, 1), "<":(0, -1), "v":(1, 0), "^":(-1, 0)}
        from collections import deque
        start_i, start_j = start[0], start[1]
        q = deque([(start_i, start_j)])
        ans[start_i][start_j] = 0

        while q:
            i, j = q.popleft()
            for x, y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= x < m and 0 <= y < n:
                    k = 0
                    if (x-i, y-j) != hash_dir[matrix[i][j]]:
                        k = 1
                    if ans[i][j] + k < ans[x][y]:
                        ans[x][y] = ans[i][j] + k
                        if k == 0:
                            q.appendleft((x, y))
                        elif k == 1:
                            q.append((x, y))
        return ans[end[0]][end[1]]

matrix = [">>v","v^<","<><"]
start = [0,1]
end = [2,0]
print(Solution().conveyorBelt(matrix, start, end))