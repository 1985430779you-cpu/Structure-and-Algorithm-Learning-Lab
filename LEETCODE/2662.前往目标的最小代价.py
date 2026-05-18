class Solution:
    def minimumCost(self, start, target, specialRoads):
        from heapq import heappop, heappush
        from collections import defaultdict
        m, n = target
        i, j = start
        dis = [[float("inf")]*(n+1) for _ in range(m+1)]
        dis[i][j] = 0
        portal = defaultdict(list)
        for x0, y0, x1, y1, c in specialRoads:
            portal[(x0, y0)].append((x1, y1, c))
        h = [(0, i, j)]

        while h:
            c, x, y = heappop(h)
            if c > dis[x][y]:
                continue

            if (x, y) in portal:
                for x1, y1, c1 in portal[(x, y)]:
                    if c + c1 < dis[x1][y1]:
                        dis[x1][y1] = c + c1
                        heappush(h, (c+c1, x1, y1))
            
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                X, Y = x+dx, y+dy
                if 0 <= X <= m and 0 <= Y <= n:
                    C = c+1
                    if  C < dis[X][Y]:
                        dis[X][Y] = C
                        heappush(h, (C, X, Y))
        return dis[-1][-1]
    
class Solution1:
    def minimumCost(self, start, target, specialRoads):
        from collections import defaultdict
        t = tuple(target)
        dis = defaultdict(lambda: float("inf"))
        dis[tuple(start)] = 0
        vis = set()

        while True:
            v, dv = None, -1
            for p, d in dis.items():
                if p not in vis and (dv < 0 or d < dv):
                    v, dv = p, d
            if v == t:
                return dv
            vis.add(v) 
            vx, vy = v
            dis[t] = min(dis[t], dv + t[0] - vx + t[1] - vy)
            for x1, y1, x2, y2, cost in specialRoads:
                w = (x2, y2)
                dis[w] = min(dis[w], dv + abs(x1 - vx) + abs(y1 - vy) + cost)

start = [24556,19664]
target = [40028,63600]
specialRoads = [[38828,26972,29584,37928,4402],[33756,22055,31073,37149,47007],[37749,34652,26833,20802,16294],[25540,44250,38439,37835,11416],[24982,43479,32467,49092,96130],[34952,40456,27981,21219,6056],[37700,26055,27828,44677,12218],[29190,27558,34831,55589,4044],[38035,61065,27064,46277,17357],[35003,21018,38616,45047,24302],[36291,21994,27413,34819,20881],[33310,57695,25317,28231,36464],[34495,36373,26111,48401,30999],[29162,23071,24858,37392,5702],[39259,44797,35961,53350,3542],[32389,51626,31282,48459,2276],[28061,43280,36064,55592,1818],[26773,31980,30032,44782,3042],[28588,60936,31930,43114,5247],[28911,32065,27725,56500,22855],[29072,53047,27661,57133,5768],[29319,62708,27007,22096,26722],[27486,20519,34879,63540,17886],[34047,62415,27646,47999,3253],[33238,44640,39064,50543,3271],[35279,32438,34767,62042,11577],[33041,55960,33421,44427,51911],[27306,61515,32140,45072,12986],[36899,27352,31436,63574,17850],[36461,37435,36431,32931,670],[35161,28104,27223,42991,13224]]
print(Solution1().minimumCost(start, target, specialRoads))