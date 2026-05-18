import heapq
class Solution:
    def solveSudoku(self, board):
        rowlist = [set() for _ in range(9)]
        collist = [set() for _ in range(9)]
        sublist = [[set() for _ in range(3)] for _ in range(3)]
        emptypos = []

        #空格子放入emptypos，数字变为int放入set
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x == ".":
                    emptypos.append((i,j))
                else:
                    rowlist[i].add(int(x))
                    collist[j].add(int(x))
                    sublist[i//3][j//3].add(int(x))

        #可选数字的长度
        def get_candidates(i, j):
            return 9 - len(rowlist[i] | collist[j] | sublist[i//3][j//3])
        #找到可选数字最少的位置，从这个位置开始做数独
        empty_heap = [(get_candidates(i, j), i, j) for (i, j) in emptypos]
        heapq.heapify(empty_heap) #排序，最小的堆叠上来

        #定义深度优先搜索
        def dfs():
            if not empty_heap:
                return True
            #依次尝试待定数字最少的位置
            _, i, j = heapq.heappop(empty_heap) #删除返回最小值，一般是empty_heap[0]
            for item in range(1, 10):
                if item in rowlist[i] or item in collist[j] or item in sublist[i//3][j//3]:
                    continue #冲突就跳过，直到不冲突，dfs()继续回溯
                board[i][j] = str(item)
                rowlist[i].add(item)
                collist[j].add(item)
                sublist[i//3][j//3].add(item)
                #回溯：最后一个空格填上后，最后一层一直返回True到顶层（实现回溯的重点！！！）
                if dfs() is True:
                    return True
                #恢复原状
                rowlist[i].remove(item)
                collist[j].remove(item)
                sublist[i//3][j//3].remove(item)
            #如果前面所有步骤都不能返回True，还原后返回False
            heapq.heappush(empty_heap, (get_candidates(i, j), i, j)) #待定数字得多少根据前面所填的数字发生改变，需要重新统计
            return False

        dfs()
        return board


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
print(sol.solveSudoku(board))