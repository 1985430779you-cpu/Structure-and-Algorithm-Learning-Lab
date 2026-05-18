class Solution:
    def updateBoard(self, board, click):
        m, n = len(board), len(board[0])
        vis = [[1]*n for _ in range(m)]
        direc = [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(1,1),(-1,-1),(-1,1)]
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        board[click[0]][click[1]] = "B"

        def search(i, j):
            bomb = 0
            for x, y in direc:
                if 0 <= i+x < m and 0 <= j+y < n and board[i+x][j+y] == "M":
                    bomb += 1
            return bomb
        
        def expansion(i, j):
            if board[i][j] != "B":
                return
            if vis[i][j] == 0:
                return
            vis[i][j] = 0
            if search(i,j) > 0:
                board[i][j] = str(search(i, j))
                return
            else:
                for x, y in direc:
                    if 0 <= i+x < m and 0 <= j+y < n and vis[i+x][j+y] != 0:
                        board[i+x][j+y] = "B"
                        expansion(i+x, j+y)

        expansion(click[0], click[1])
        return board

board = [["E","E","E","E","E"],
         ["E","E","M","E","E"],
         ["E","E","E","E","E"],
         ["E","E","E","E","E"]]
click = [3,0]
sol = Solution()
print(sol.updateBoard(board, click))