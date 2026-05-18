class Solution:
    def solve(self, board):
        m, n = len(board), len(board[0])
        pos = [[1]*n for _ in range(m)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if board[i][j] == "X":
                return 0
            if pos[i][j] == 0:
                return 0
            pos[i][j] = 0
            path.append((i, j))
            return max(dfs(i+1,j), dfs(i-1,j), dfs(i,j+1), dfs(i,j-1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and pos[i][j] == 1:
                    path = []
                    a = dfs(i, j)
                    if a == 0:
                        for x, y in path:
                            board[x][y] = "X"   
        return board

board = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
sol = Solution()
print(sol.solve(board))