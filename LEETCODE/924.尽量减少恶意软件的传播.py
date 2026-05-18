class Solution:
    def minMalwareSpread(self, graph, initial):
        n = len(graph)
        g = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1 and i != j:
                    g[i].append(j)
        
        vis = [0]*n
        results = []
        def dfs(x):
            vis[x] = 1
            path.append(x)
            for y in g[x]:
                if vis[y] == 0:
                    dfs(y)

        ans = n
        initial.sort()
        for error in initial:
            if vis[error] == 0:
                path = []
                dfs(error)
                results.append(path)
            elif vis[error] == 1:
                for i in range(len(results)):
                    if error in results[i]:
                        ans = min(ans, results[i][0])
                        results[i] = []
        
        length = 0
        for i in range(len(results)):
            if len(results[i]) > length:
                length = len(results[i])
                ans = results[i][0]

        return ans
    
class Solution1:
    def minMalwareSpread(self, graph, initial):
        from collections import defaultdict
        n = len(graph)
        g = [[]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and graph[i][j] == 1:
                    g[i].append(j)
        
        un = list(range(n))
        def find(x):
            if x != un[x]:
                un[x] = find(un[x])
            return un[x]
        
        for a in range(n):
            for b in g[a]:
                if find(a) != find(b):
                    un[find(a)] = find(b)
        
        dict1 = defaultdict(set)
        dict2 = defaultdict(int)
        for i in range(n):
            dict1[find(i)].add(i)
            if i in initial:
                dict2[find(i)] += 1
        
        initial.sort()
        length = -1
        ans = 0
        for i in initial:
            ri = find(i)
            if dict2[ri] == 1:
                if len(dict1[find(i)]) > length:
                    length = len(dict1[find(i)])
                    ans = i
            elif dict2[find(i)] > 1:
                if 0 > length:
                    length = 0
                    ans = i
        return ans

graph = [[1,1,0],[1,1,0],[0,0,1]]
initial = [0,1]
print(Solution1().minMalwareSpread(graph, initial))    