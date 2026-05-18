class Solution:
    def isValidSudouku(self, board):
        rowlist = set()
        collist = set()
        sublist = set()

        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x == ".":
                    continue
                if (i, x) in rowlist or (j, x) in collist or (i//3, j//3, x) in sublist:
                    return False
                
                rowlist.add((i, x))
                collist.add((j, x))
                sublist.add((i//3, j//3, x))
        return True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
print(sol.isValidSudouku(board))