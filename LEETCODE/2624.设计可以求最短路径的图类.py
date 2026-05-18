class Graph:
    def __init__(self, n, edges):
        g = [[] for _ in range(n)]
        for x, y, t in edges:
            g[x].append((y, t))
        self.n = n
        self.g = g        

    def addEdge(self, edge):
        self.g[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1, node2):
        from heapq import heappop, heappush
        dis = [float("inf")]*self.n
        dis[node1] = 0
        h = [(0, node1)]
        while h:
            xc, x = heappop(h)
            if xc > dis[x]:
                continue
            for y, dc in self.g[x]:
                yc = xc + dc
                if yc < dis[y]:
                    dis[y] = yc
                    heappush(h, (yc, y))
        return dis[node2] if dis[node2] < float("inf") else -1           