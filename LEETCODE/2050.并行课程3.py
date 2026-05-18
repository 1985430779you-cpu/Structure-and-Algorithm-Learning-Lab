class Solution:
    def minimumTime(self, n, relations, time):
        from collections import deque
        g = [[] for _ in range(n+1)]
        g_rev = [[] for _ in range(n+1)]
        prev = [0]*(n+1)
        for x, y in relations:
            g[x].append(y)
            prev[y] += 1

        q = deque([])
        for i in range(1, n+1):
            if prev[i] == 0:
                q.append(i)
        
        while q:
            x = q.popleft()
            if g_rev[x]:
                time[x-1] += max(g_rev[x])
            for y in g[x]:
                prev[y] -= 1
                g_rev[y].append(time[x-1])
                if prev[y] == 0:
                    q.append(y)
        return max(time)
    
n = 5
relations = [[1,5],[2,5],[3,5],[3,4],[4,5]]
time = [1,2,3,4,5]
print(Solution().minimumTime(n, relations, time))