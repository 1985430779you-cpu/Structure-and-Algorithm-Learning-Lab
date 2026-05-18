class Solution:
    def containVirus(self, isInfected):
        m, n = len(isInfected), len(isInfected[0])
        record = [[1]*n for _ in range(m)]
        queue = []
        isolate_plate = 0

        def detectVirus():
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        return True
            return False

        def calculate_perimeter(i, j):
            vis = [[1]*n for _ in range(m)]
            def dfs(x, y):
                if x < 0 or x >= m or y < 0 or y >= n:
                    return 0
                if isInfected[x][y] == 0:
                    return 1
                if isInfected[x][y] == 2:
                    return 0
                if vis[x][y] == 0:
                    return 0
                vis[x][y] = 0
                s = 0
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    s += dfs(x+dx, y+dy)
                return s
            perimeter = dfs(i, j)
            return perimeter
        
        def isolation_virus(i, j):
            vis = [[1]*n for _ in range(m)]
            def dfs(x, y):
                if x < 0 or x >= m or y < 0 or y >= n:
                    return
                if vis[x][y] == 0:
                    return
                vis[x][y] = 0
                if isInfected[x][y] == 0:
                    return
                if isInfected[x][y] == 1:
                    isInfected[x][y] = 2
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    dfs(x+dx, y+dy)
            dfs(i, j)

        for i in range(m):
            for j in range(n):
                if isInfected[i][j] == 1:
                    queue.append((i, j))
                    record[i][j] = 0

        while detectVirus():    
            mx = 0
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and calculate_perimeter(i, j) >= mx:
                        tmpi, tmpj = i, j
                        mx = calculate_perimeter(i, j)
            isolation_virus(tmpi, tmpj)
            isolate_plate += mx
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 2:
                        if (i, j) in queue:
                            queue.remove((i, j))                            
            
            if queue:
                tmp = queue
                queue = []
                for a, b in tmp:
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        x, y = a + dx, b + dy
                        if 0 <= x < m and 0 <= y < n and record[x][y] == 1 and isInfected[x][y] == 0:
                            isInfected[x][y] = 1
                            queue.append((x, y))
                            record[x][y] = 0
        return isolate_plate
    
isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
print(Solution().containVirus(isInfected))