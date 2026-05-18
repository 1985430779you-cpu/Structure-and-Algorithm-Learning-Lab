class Solution:
    def solveNQueens(self, n):
        ans = []
        path = [["." for _ in range(n)] for _ in range(n)]
        rows = [[] for _ in range(n)]
        cols = [[] for _ in range(n)]

        def has_oblique(array, i, j):
            direction = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

            for di, dj in direction:
                x, y = i + di, j + dj
                while 0 <= x < n and 0 <= y < n:
                    if array[x][y] == "Q":
                        return False
                    x += di
                    y += dj
            return True

        def dfs(row):
            if row == n:
                ans.append(["".join(row) for row in path[:]])
                return
            
            for col in range(0, n):
                if "Q" in rows[row] or "Q" in cols[col] or not has_oblique(path, row, col):
                    continue

                path[row][col] = "Q"
                rows[row].append("Q")
                cols[col].append("Q")

                dfs(row+1)

                
                path[row][col] = "."
                rows[row].remove("Q")
                cols[col].remove("Q")
            
            return False
        
        dfs(0)
        return len(ans)
    
n = 4
sol = Solution()
print(sol.solveNQueens(n)) 