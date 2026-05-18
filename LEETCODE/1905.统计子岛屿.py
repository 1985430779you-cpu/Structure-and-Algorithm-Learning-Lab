class Solution:
    def countSubIslands(self, grid1, grid2):
        m, n = len(grid1), len(grid1[0])
        pos1 = [[1]*n for _ in range(m)]
        pos2 = [[1]*n for _ in range(m)]
        cnt = 0

        def dfs1(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid1[i][j] == 0:
                return
            if pos1[i][j] == 0:
                return
            pos1[i][j] = 0
            path1.append((i, j))
            dfs1(i-1,j)
            dfs1(i+1,j)
            dfs1(i,j-1)
            dfs1(i,j+1)
            pos1[i][j] = 1

        def dfs2(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid2[i][j] == 0:
                return
            if pos2[i][j] == 0:
                return
            pos2[i][j] = 0
            path2.append((i, j))
            dfs2(i-1,j)
            dfs2(i+1,j)
            dfs2(i,j-1)
            dfs2(i,j+1)

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and pos2[i][j] == 1:
                    path1, path2 = [], []
                    dfs1(i, j)
                    dfs2(i, j)
                    if set(path2).issubset(set(path1)):
                        cnt += 1
        return cnt
    
class Solution1:
    def countSubIslands(self, grid1, grid2):
        m, n = len(grid1), len(grid1[0])
        pos = [[1]*n for _ in range(m)]
        cnt = 0

        def dfs(i, j):
            nonlocal sub
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid2[i][j] == 0 or pos[i][j] == 0:
                return
            pos[i][j] = 0
            if grid1[i][j] == 0:
                sub = False
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and pos[i][j] == 1:
                    sub = True
                    dfs(i, j)
                    if sub:
                        cnt += 1
        return cnt
    
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
sol = Solution1()
print(sol.countSubIslands(grid1, grid2))