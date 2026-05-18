class Solution:
    def slidingPuzzle(self, board):
        from collections import deque
        initial = ""
        for i in range(2):
            for j in range(3):
                initial += str(board[i][j])
                if board[i][j] == 0:
                    start_i, start_j = i, j

        q = deque([(start_i, start_j, initial)])
        record = {initial}
        cnt = 0
        while q:
            tmp = q
            q = []
            for i, j, string in tmp:
                if string == "123450":
                    return cnt
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    x, y = i+dx, j+dy
                    if 0 <= x < 2 and 0 <= y < 3:
                        a = i*3+j
                        b = x*3+y
                        posi, posj = x, y
                        if a > b:
                            a, b = b, a
                        new_string = string[:a] + string[b] + string[a+1:b] + string[a] + string[b+1:]
                        if new_string not in record:
                            q.append((posi, posj, new_string))
                            record.add(new_string)
            cnt+= 1
        return -1

board = [[1,2,3],[4,0,5]]
print(Solution().slidingPuzzle(board))