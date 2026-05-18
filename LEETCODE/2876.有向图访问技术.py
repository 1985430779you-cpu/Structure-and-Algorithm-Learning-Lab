class Solution:
    def countVisitedNodes(self, edges):
        from collections import deque, defaultdict
        n = len(edges)
        prev = [0]*n
        r_edges = [[] for _ in range(n)]
        for i in range(n):
            prev[edges[i]] += 1
            r_edges[edges[i]].append(i)

        q = deque([])
        for i in range(n):
            if prev[i] == 0:
                q.append(i)
        while q:
            x = q.popleft()
            y = edges[x]
            prev[y] -= 1
            if prev[y] == 0:
                q.append(y)

        dis = list(range(n))
        def find(x):
            if dis[x] != x:
                dis[x] = find(dis[x])
            return dis[x]
        for i in range(n):
            if prev[i] == 1 and prev[edges[i]] == 1:
                dis[find(i)] = find(edges[i])
            else:
                dis[i] = -1
        
        ring_length = defaultdict(int)
        for i in range(n):
            if dis[i] != -1:
                ring_length[find(dis[i])] += 1
        
        ans = [-1]*n
        for i in range(n):
            if prev[i] == 1:
                ans[i] = ring_length[find(i)]
                Q = deque([i])
                k = 0
                while Q:
                    tmp = Q
                    Q = []
                    for x in tmp:
                        for y in r_edges[x]:
                            if prev[y] == 0:
                                Q.append(y)
                                ans[y] = ring_length[find(i)] + k + 1
                    k += 1
        return ans               

edges = [7,0,7,0,5,3,3,0]
print(Solution().countVisitedNodes(edges))