#复习掩码思路和多维数组
class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        rubbish = [[0] * n for _ in range(m)]
        cnt_l, start_i, start_j = 0, 0, 0
        ans = 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "L":
                    rubbish[i][j] = 1 << cnt_l
                    cnt_l += 1
                elif classroom[i][j] == "S":
                    start_i, start_j = i, j
        if cnt_l == 0:
            return ans
        vis = [[[[1]*(1 << cnt_l) for _ in range(energy+1)] for _ in range(n)] for _ in range(m)]
        q = [(start_i, start_j, energy, 0)]
        vis[start_i][start_j][energy][0] = 0
        while q:
            tmp = q
            q = []
            for X, Y, E, L in tmp:
                if L == (1 << cnt_l) - 1:
                    return ans
                if E == 0:
                    continue
                for dX, dY in (1, 0), (-1, 0), (0, 1), (0, -1):
                    x, y = X+dX, Y+dY
                    if 0 <= x < m and 0 <= y < n and classroom[x][y] != "X":
                        cur_e = energy if classroom[x][y] == "R" else E-1
                        l = L | rubbish[x][y]
                        if vis[x][y][cur_e][l] == 1:
                            q.append((x, y, cur_e, l))
                            vis[x][y][cur_e][l] = 0
            ans += 1
        return -1

classroom = classroom = ["L.S", "RXL"]
energy = 3
print(Solution().minMoves(classroom, energy))