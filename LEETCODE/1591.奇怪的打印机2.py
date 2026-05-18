class Solution:
    def isPrintable(self, targetGrid):
        from collections import deque
        m, n = len(targetGrid), len(targetGrid[0])
        colors = set()
        l = max(max(targetGrid[i]) for i in range(m))
        left = [float("inf")]*(l+1)
        right = [0]*(l+1)
        up = [float("inf")]*(l+1)
        down = [0]*(l+1)
        for i in range(m):
            for j in range(n):
                color = targetGrid[i][j]
                left[color] = min(j, left[color])
                right[color] = max(j, right[color])
                up[color] = min(i, up[color])
                down[color] = max(i, down[color])
                colors.add(color)

        colors = list(colors)
        g = [[] for _ in range(l+1)]
        prev = [0]*(l+1)
        for value in colors:
            for x in range(up[value], down[value]+1): 
                for y in range(left[value], right[value]+1):
                    if targetGrid[x][y] != value:
                        if targetGrid[x][y] not in g[value]:
                            g[value].append(targetGrid[x][y])
                            prev[targetGrid[x][y]] += 1
        
        q = deque([])
        for i in range(l+1):
            if prev[i] == 0 and i in colors:
                q.append(i)
        while q:
            x = q.popleft()
            for y in g[x]:
                prev[y] -= 1
                if prev[y] == 0:
                    q.append(y)
        return all(prev[i]==0 for i in range(len(prev)))
        

targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
print(Solution().isPrintable(targetGrid))