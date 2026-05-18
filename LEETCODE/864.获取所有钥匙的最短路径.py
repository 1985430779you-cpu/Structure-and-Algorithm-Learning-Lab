class Solution:
    def shortestPathAllKeys(self, grid):
        m, n = len(grid), len(grid[0])
        key = [[0]*n for _ in range(m)]
        hash_key = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5}
        hash_door = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
        maximum_key_num = -1
        start_i, start_j = 0, 0
        for i in range(m):
            for j in range(n):
                if "a" <= grid[i][j] <= "f":
                    key[i][j] = 1 << hash_key[grid[i][j]]
                    maximum_key_num = max(maximum_key_num, hash_key[grid[i][j]])
                elif grid[i][j] == "@":
                    start_i, start_j = i, j
        if maximum_key_num < 0:
            return 0
        num = 1 << (maximum_key_num+1)
        vis = [[[0]*num for _ in range(n)] for _ in range(m)]
        q = [(start_i, start_j, 0)]
        ans = 0

        while q:
            tmp = q
            q = []
            for X, Y, K in tmp:
                if K == num-1:
                    return ans
                for dX, dY in (1, 0), (-1, 0), (0, 1), (0, -1):
                    x, y = X+dX, Y+dY
                    check = True
                    if 0 <= x < m and 0 <= y < n and grid[x][y] != "#":
                        if "A" <= grid[x][y] <= "F":
                            #if K | (1 << (hash_door[grid[x][y]])) != K:
                            if not (K >> hash_door[grid[x][y]] & 1):
                                check = False
                        k = K | key[x][y]
                        if vis[x][y][k] == 0 and check:
                            q.append((x, y, k))
                            vis[x][y][k] = 1
            ans += 1
        return -1
    
grid = ["@.a..","###.#","b.A.B"]
print(Solution().shortestPathAllKeys(grid))  