class Solution:
    def networkBecomesIdle(self, edges, patience):
        from collections import deque
        n = len(patience)
        g = [[] for _ in range(n)]
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)
        
        vis = [-1]*n
        vis[0] = 0
        q = deque([0])
        while q:
            x = q.popleft()
            for y in g[x]:
                if vis[y] < 0:
                    vis[y] = vis[x]+1
                    q.append(y)
        
        max_t = 0
        for i in range(1, n):
            if 2*vis[i] % patience[i] == 0:
                times = 2*vis[i] // patience[i] - 1
            else:
                times = 2*vis[i] // patience[i]
            t = times*patience[i] + vis[i]*2 + 1
            max_t = max(max_t, t)
        return max_t

edges = [[0,1],[1,2]]
patience = [0,2,1]
print(Solution().networkBecomesIdle(edges, patience))