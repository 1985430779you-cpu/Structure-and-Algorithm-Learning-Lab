class Solution:
    def solveNQueens(self, n):
        ans = []
        path = [["." for _ in range(n)] for _ in range(n)]
        rows = [[] for _ in range(n)]
        cols = [[] for _ in range(n)]

        def dfs(row):
            if row == n:
                ans.append(["".join(row) for row in path])
                return
            
            def hasOblique(a, i, j):
                directions = [(-1, -1), (-1, 1)] #由于按顺序，只需检查左上和右上

                for di, dj in directions:
                    x = i + di
                    y = j + dj
                    while 0 <= x < n and 0 <= y < n:
                        if a[x][y] == "Q":
                            return False
                        x += di
                        y += dj
                return True    
            
            for j in range(n):
                if "Q" in rows[row] or "Q" in cols[j] or not hasOblique(path, row, j):
                    continue
                path[row][j] = "Q"
                rows[row].append("Q")
                cols[j].append("Q")

                dfs(row+1)
            
                path[row][j] = "."
                rows[row].remove("Q")
                cols[j].remove("Q")
            
            return False
        
        dfs(0)
        return ans
    
n = 4
sol = Solution()
print(sol.solveNQueens(n))    