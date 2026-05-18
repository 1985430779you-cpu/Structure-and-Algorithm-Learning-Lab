class Solution:
    def minimumCost(self, n, edges, query):
        from collections import defaultdict
        g = list(range(n))

        def find(x):
            if g[x] != x:
                g[x] = find(g[x])
            return g[x]
        
        for a, b, _ in edges:
            fa, fb = find(a), find(b)
            if fa != fb:
                g[fa] = fb
        
        path = {}
        for a, b, c in edges:
            if find(a) not in path:
                path[find(a)] = c
            else:
                path[find(a)] &= c
        
        ans = []
        for i, j in query:
            if i == j:
                ans.append(0)
            if find(i) != find(j):
                ans.append(-1)
            else:
                ans.append(path[find(i)])
        
        return ans

n = 5
edges = [[0,1,7],[1,3,7],[1,2,1]]
query = [[0,3],[3,4]]
print(Solution().minimumCost(n, edges, query))