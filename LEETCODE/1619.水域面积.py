class Solution:
    def pondSizes(self, land):
        m, n = len(land), len(land[0])
        pos = [[1]*n for _ in range(m)]
        ans = []

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if land[i][j] > 0:
                return 0
            if pos[i][j] == 0:
                return 0
            pos[i][j] = 0
            s = 1
            s += dfs(i-1,j)
            s += dfs(i+1,j)
            s += dfs(i,j-1)
            s += dfs(i,j+1)
            s += dfs(i-1,j+1)
            s += dfs(i+1,j+1)
            s += dfs(i-1,j-1)
            s += dfs(i+1,j-1)
            return s
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0 and pos[i][j] == 1:
                    ans.append(dfs(i, j))
        ans.sort()
        return ans
    
grid = [[0,2,1,0],
        [0,1,0,1],
        [1,1,0,1],
        [0,1,0,1]]
sol = Solution()
print(sol.pondSizes(grid))   