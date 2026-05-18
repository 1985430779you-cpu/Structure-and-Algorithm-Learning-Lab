class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        g = [[] for _ in range(n)]
        prev = [0]*n
        for x, y in edges:
            g[x].append(y)
            prev[y] += 1
        
        ans = []
        for i in range(n):
            if prev[i] == 0:
                ans.append(i)
        return ans
n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
print(Solution().findSmallestSetOfVertices(n, edges))