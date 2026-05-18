#困难题：位运算
class Solution:
    def numberOfSets(self, n, maxDistance, roads):
        g = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            g[i][i] = 0
        for x, y, wt in roads:
            g[x][y] = min(g[x][y], wt)
            g[y][x] = min(g[y][x], wt)

        f = [None] * n
        # s表示当前的保留点集合，根据它去算距离
        def check(s: int) -> int:
            for i, row in enumerate(g):
                if s >> i & 1:  # i 在集合 s 中，说明这个点要保留，将它的邻接关系录入
                    f[i] = row.copy()

            # Floyd 算法（只考虑在 s 中的节点）
            for k in range(n):
                if (s >> k & 1) == 0:  # k 不在集合 s 中
                    continue
                for i in range(n):
                    if (s >> i & 1) == 0 or f[i][k] == float("inf"):  # 当前点不可达
                        continue
                    for j in range(n):  # 经典floyd更新最小
                        f[i][j] = min(f[i][j], f[i][k] + f[k][j])

            # 判断保留的节点之间的最短路是否均不超过 maxDistance
            for i, di in enumerate(f):
                if (s >> i & 1) == 0:  # i 不在集合 s 中
                    continue
                for j, dij in enumerate(di):  # 判断第i个点与第j个点的距离
                    if s >> j & 1 and dij > maxDistance:
                        return 0
            return 1

        # 枚举子集 s，作为保留的节点，判断这些节点否满足要求
        return sum(check(s) for s in range(1 << n))

n = 3 
maxDistance = 5
roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
print(Solution().numberOfSets(n, maxDistance, roads))