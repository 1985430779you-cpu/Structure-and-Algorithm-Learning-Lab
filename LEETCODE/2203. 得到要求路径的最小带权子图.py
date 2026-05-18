#重点复习套路
class Solution:
    def minimumWeight(self, n, edges, src1, src2, dest):
        from heapq import heappop, heappush
        from collections import deque       
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        for x, y, c in edges:
            g[x].append((y, c))
            rg[y].append((x, c))
        
        def dijkstra(start, graph):
            dis = [float("inf")]*n
            dis[start] = 0
            h = [(0, start)]
            while h:
                xc, x = heappop(h)
                if xc > dis[x]:
                    continue         
                for y, dc in graph[x]:
                    yc = xc + dc
                    if yc < dis[y]:
                        dis[y] = yc
                        heappush(h, (yc, y))
            return dis
        
        #dis1+dis2：src1和src2到交点的距离；dis3:终点到交点的距离
        dis1 = dijkstra(src1, g)
        dis2 = dijkstra(src2, g)
        dis3 = dijkstra(dest, rg)
        
        ans = float('inf')
        for i in range(n):
            if dis1[i] < float('inf') and dis2[i] < float('inf') and dis3[i] < float('inf'):
                ans = min(ans, dis1[i] + dis2[i] + dis3[i])
        
        return ans if ans < float('inf') else -1  
    
n = 6 
edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]
src1 = 0
src2 = 1
dest = 5
print(Solution().minimumWeight(n, edges, src1, src2, dest))