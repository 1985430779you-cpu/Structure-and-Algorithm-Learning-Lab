class Solution:
    def loudAndRich(self, richer, quiet):
        from collections import deque
        n = len(quiet)
        ans = list(range(n))
        g = [[] for _ in range(n)]
        prev = [0]*n
        for x, y in richer:
            g[x].append(y)
            prev[y] += 1

        q = deque([])
        for i in range(n):
            if prev[i] == 0:
                q.append(i)
        
        while q:
            x = q.popleft()
            for y in g[x]:
                prev[y] -= 1
                if quiet[ans[x]] < quiet[ans[y]]:
                    ans[y] = ans[x]
                if prev[y] == 0:
                    q.append(y)
        return ans
    
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
print(Solution().loudAndRich(richer, quiet))