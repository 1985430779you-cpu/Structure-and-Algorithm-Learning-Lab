class Solution:
    def countOfPairs(self, n, x, y):
        from collections import deque
        g = [[] for _ in range(n+1)]
        for i in range(1, n):
            g[i].append(i+1)
            g[i+1].append(i)
        g[x].append(y)
        g[y].append(x)
        
        ans = [0]*n
        for i in range(1, n+1):
            vis = [-1]*(n+1)
            vis[i] = 0
            q = deque([i])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if vis[y] < 0:
                        vis[y] = vis[x]+1
                        q.append(y)
            for j in vis:
                if j > 0:
                    ans[j-1] += 1
        
        return ans
    
n = 3
x = 1
y = 3
print(Solution().countOfPairs(n, x, y))