#入度全为1，用并查集找
#入度为2，一定是删除某一条边
class Solution:
    def findRedundantDirectedConnection(self, edges):     
        n = len(edges)
        g = [[] for _ in range(n+1)]
        prev = [0]*(n+1)
        for x, y in edges:
            g[y].append(x)
            prev[y] += 1

        dis = list(range(0, n+1))
        def find(x):
            if dis[x] != x:
                dis[x] = find(dis[x])
            return dis[x]       
        def union(a, b):
            dis[find(a)] = find(b)
        
        if all(prev[i] != 2 for i in range(1, n+1)):
            for x, y in edges:
                if find(x) != find(y):
                    union(x, y)
                else:
                    return[x, y]
        else:
            j = prev.index(2)
            remove = []
            for i in g[j]:
                remove.append((i, j))
            for x, y in edges:
                if (x, y) not in remove:
                    union(x, y)
            for a, b in remove:
                if find(a) != find(b):
                    union(a, b)
                else:
                    return[a, b]            

edges = [[1,2],[1,3],[2,3]]
print(Solution().findRedundantDirectedConnection(edges))