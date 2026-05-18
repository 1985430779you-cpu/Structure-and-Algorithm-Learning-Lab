class Solution:
    def minMaxWeight(self, n, edges, threshold):
        from collections import deque
        #最短路
        def bfs(mid):
            r_g = [[] for _ in range(n)]
            for x, y, c in edges:
                if c > mid:
                    continue
                r_g[y].append(x)
                
            vis = [-1]*n
            q = deque([0])
            while q:
                x = q.popleft()
                vis[x] = 0
                for y in r_g[x]:
                    if vis[y] == -1:
                        vis[y] = 0
                        q.append(y)
            return all(vis[i] == 0 for i in range(n))
        
        #二分法
        mx = max(edges[i][2] for i in range(len(edges)))
        low, high = 0, mx
        while low <= high:
            mid = (low+high) // 2
            if bfs(mid):
                high = mid-1
            else:
                low = mid+1
        return low if low <= mx else -1

n = 4
edges = [[2,0,39],[2,1,72],[2,3,67],[1,2,78],[3,0,10],[0,2,81]]
threshold = 2
print(Solution().minMaxWeight(n, edges, threshold))