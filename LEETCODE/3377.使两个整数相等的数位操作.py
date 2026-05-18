class Solution:
    def minOperations(self, n, m):
        #埃式筛法
        prime = ["True"]*10000
        prime[1] = False
        for x in range(2, 10000):
            if prime[x]:
                for y in range(x**2, 10000, x):
                    prime[y] = False
        
        from heapq import heappop, heappush
        if prime[n] or prime[m]:
            return -1
        l = len(str(n))
        dis = [float("inf")]*(10**l)
        dis[n] = n
        h = [(n, n)]

        while h:
            c, x = heappop(h)
            if x == m:
                return c
            if c > dis[x]:
                continue
            x0 = x
            cnt = 0
            while x0 != 0:
                x_mod = x0 % 10
                x_div = x0 // 10
                if x_mod == 0:
                    y = x+1*10**cnt
                    if not prime[y] and c+y < dis[y]:
                        dis[y] = c+y
                        heappush(h, (c+y, y))
                elif x_mod == 9:
                    y = x-1*10**cnt
                    if not prime[y] and c+y < dis[y]:
                        dis[y] = c+y
                        heappush(h, (c+y, y))                    
                else:
                    for choice in 1, -1:
                        y = x+choice*10**cnt
                        if not prime[y] and len(str(y)) == l and c+y < dis[y]:
                            dis[y] = c+y
                            heappush(h, (c+y, y))
                cnt += 1
                x0 = x_div
        return -1

n = 10
m = 12
print(Solution().minOperations(n, m))