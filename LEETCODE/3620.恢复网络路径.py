#二分记忆化搜索：最大值最小，最小值最大，考虑二分
class Solution:
    def findMaxPathScore(self, edges, online, k):
        from collections import deque
        from functools import cache
        n = len(online)
        g = [[] for _ in range(n)]
        for x, y, c in edges:
            if online[x] and online[y]:
                g[x].append((y, c))

        def check(ans):
            @cache
            def dfs(x):
                if x == n-1:
                    return 0
                init = float("inf")
                for y, c in g[x]:
                    if c >= ans:
                        init = min(init, dfs(y)+c)
                return init
            if dfs(0) <= k:
                return True
            return False

        low, high = 0, k
        while low < high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid
        return low-1

edges = [[2,3,50],[3,4,65],[0,1,91],[1,4,47],[0,3,24],[1,3,53]]
online = [True,True,True,True,True]
k = 254
print(Solution().findMaxPathScore(edges, online, k))