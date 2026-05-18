class Solution:
    def buildMatrix(self, k, rowConditions, colConditions):
        from collections import deque
        matrix = [[0]*k for _ in range(k)]
        g_row = [[] for _ in range(k)]
        prev_row = [0]*k
        g_col = [[] for _ in range(k)]
        prev_col = [0]*k
        for i, j in rowConditions:
            g_row[i-1].append(j-1)
            prev_row[j-1] += 1
        for x, y in colConditions:
            g_col[x-1].append(y-1)
            prev_col[y-1] += 1      

        def bfs(g, prev):
            q = deque([])
            for i in range(len(prev)):
                if prev[i] == 0:
                    q.append(i)
            ans = []
            while q:
                x = q.popleft()
                ans.append(x)
                for y in g[x]:
                    prev[y] -= 1
                    if prev[y] == 0:
                        q.append(y)
            if len(ans) < len(prev):
                return []
            return ans

        row, col = bfs(g_row, prev_row), bfs(g_col, prev_col)
        if not row or not col:
            return []
        for i in range(k):
            matrix[row.index(i)][col.index(i)] = i+1
        return matrix       

k = 3
rowConditions = [[1,2],[3,2]] 
colConditions = [[2,1],[3,2]]
print(Solution().buildMatrix(k, rowConditions, colConditions))            