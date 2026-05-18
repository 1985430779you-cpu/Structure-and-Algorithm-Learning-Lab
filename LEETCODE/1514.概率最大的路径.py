class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        from heapq import heappop, heappush
        g = [[] for _ in range(n)]
        for i in range(len(edges)):
            g[edges[i][0]].append((edges[i][1], succProb[i]))
            g[edges[i][1]].append((edges[i][0], succProb[i]))
        dis = [0]*n
        dis[start_node] = 1
        h = [(-1, start_node)]

        while h:
            xp, x = heappop(h)
            xp = -xp
            if xp > dis[x]:
                continue
            for y, dp in g[x]:
                yp = xp*dp
                if dis[y] == 0 or yp > dis[y]:
                    dis[y] = yp
                    heappush(h, (-yp, y))        
        return dis[end_node]
    
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
print(Solution().maxProbability(n, edges, succProb, start, end))