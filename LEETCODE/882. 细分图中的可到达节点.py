class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        from heapq import heappop, heappush
        g = [[] for _ in range(n)]
        for x, y, c in edges:
            g[x].append((y, c+1))
            g[y].append((x, c+1))
        dis = [float("inf")]*n
        dis[0] = 1
        h = [(1, 0)]
        while h:
            xc, x = heappop(h)
            if xc > dis[x]:
                continue
            for y, dc in g[x]:
                yc = xc + dc
                if yc < dis[y]:
                    dis[y] = yc
                    heappush(h, (yc, y))
        
        total = 0
        for i in dis:
            if i <= maxMoves+1:
                total += 1
        
        for x, y, c in edges:
            mx1 = mx2 = 0
            if dis[x] <= maxMoves:
                mx1 = maxMoves - dis[x] + 1
            if dis[y] <= maxMoves:
                mx2 = maxMoves - dis[y] + 1
            mx = mx1 + mx2
            if mx <= c:
                total += mx
            else:
                total += c
        return total            

edges = [[1,2,5],[0,3,3],[1,3,2],[2,3,4],[0,4,1]]
maxMoves = 7
n = 5
print(Solution().reachableNodes(edges, maxMoves, n))