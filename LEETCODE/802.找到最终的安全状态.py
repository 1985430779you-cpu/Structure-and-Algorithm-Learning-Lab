class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        vis = [0]*n
        def dfs(x):
            vis[x] = 1
            for y in graph[x]:
                if vis[y] == 1 or vis[y] == 0 and dfs(y):
                    return True
            vis[x] = 2
            return False
        
        ans = []
        for i in range(n):
            if vis[i] == 2 or vis[i] == 0 and not dfs(i):
                ans.append(i)
        return ans

class Solution1:
    def eventualSafeNodes(self, graph):
        from collections import deque
        n = len(graph)
        g = [[] for _ in graph]
        for x in range(n):
            for y in graph[x]:
                g[y].append(x)
        prev = [len(ys) for ys in graph]
        
        q = deque([])
        for i in range(n):
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
        ans.sort()
        return ans

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(Solution1().eventualSafeNodes(graph))    
