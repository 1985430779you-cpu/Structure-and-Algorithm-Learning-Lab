class Solution:
    def minMoves(self, matrix):
        from collections import deque
        from collections import defaultdict
        if matrix[-1][-1] == '#':
            return -1
        
        m, n = len(matrix), len(matrix[0])
        pos = defaultdict(list)
        for i in range(m):
            for j in range(n):
                if "A" <= matrix[i][j] <= "Z":
                    pos[matrix[i][j]].append((i, j))

        ans = [[float("inf")]*n for _ in range(m)]
        q = deque([(0, 0)])
        ans[0][0] = 0

        while q:
            i, j = q.popleft()
            d = ans[i][j]
            if i == m-1 and j == n-1:
                return d
            
            if matrix[i][j] in pos:
                for x, y in pos[matrix[i][j]]:
                    if d < ans[x][y]:
                        ans[x][y] = d
                        q.appendleft((x, y))
                del pos[matrix[i][j]]
            
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] != "#" and d+1 < ans[x][y]:
                    q.append((x, y))
                    ans[x][y] = d+1
        
        return -1
    
matrix = ["A..",".A.","..."]    
print(Solution().minMoves(matrix))              