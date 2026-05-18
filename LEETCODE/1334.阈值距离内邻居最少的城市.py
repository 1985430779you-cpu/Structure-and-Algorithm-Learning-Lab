class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        f = [[float("inf")]*n for _ in range(n)]
        for i in range(n):
            f[i][i] = 0       
        for x, y, w in edges:
            f[x][y] = min(f[x][y], w)
            f[y][x] = min(f[y][x], w)
        
        for k in range(n):
            for i in range(n):
                if f[i][k] == float("inf"):
                    continue
                for j in range(n):
                    f[i][j] = min(f[i][j], f[i][k]+f[k][j])
        
        count = n
        ans = -1
        for i, row in enumerate(f):
            s = sum(num <= distanceThreshold for num in row)
            if s <= count and i > ans:
                count = s
                ans = i
        
        return ans
    
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
print(Solution().findTheCity(n, edges, distanceThreshold))