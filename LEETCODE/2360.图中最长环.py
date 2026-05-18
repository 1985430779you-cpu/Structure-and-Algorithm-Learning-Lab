class Solution:
    def longestCycle(self, edges):
        from collections import deque
        n = len(edges)
        prev = [0]*n
        for i in range(n):
            if edges[i] != -1:
                j = edges[i]
                prev[j] += 1
        
        q = deque([])
        for i in range(n):
            if prev[i] == 0:
                q.append(i)
        while q:
            x = q.popleft()
            if edges[x] == -1:
                continue
            y = edges[x]
            prev[y] -= 1
            if prev[y] == 0:
                q.append(y)
        
        ans = -1
        for i in range(n):
            if prev[i] == 1:
                length = 1
                prev[i] -= 1
                q1 = deque([i])
                while q1:
                    x1 = q1.popleft()
                    y1 = edges[x1]
                    if prev[y1] == 1:
                        prev[y1] -= 1
                        q1.append(y1)
                        length += 1
                ans = max(ans, length)
        return ans

edges = [-1,2,1]
print(Solution().longestCycle(edges))