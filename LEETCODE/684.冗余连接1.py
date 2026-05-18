#父节点相同的点连接会导致环
class Solution:
    def findRedundantConnection(self, edges):
        from collections import deque
        n = len(edges)
        dis = list(range(0, n+1))

        def find(x):
            if dis[x] != x:
                dis[x] = find(dis[x])
            return dis[x]
        
        def union(a, b):
            dis[find(a)] = find(b)

        for x, y in edges:
            if find(x) != find(y):
                union(x, y)
            else:
                return[x, y]

edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print(Solution().findRedundantConnection(edges))