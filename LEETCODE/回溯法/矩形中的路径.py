class Solution:
    def hasPath(self, string, matrix):
        n = len(string)
        rows = len(matrix)
        cols = len(matrix[0])
        if n == 0:
            return True
        if rows == 0 or cols == 0:
            return False
        
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        def dfs(i, row, col):
            if i == n:
                return True           
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if visited[row][col]:
                return False
            if matrix[row][col] != string[i]:
                return False
            
            visited[row][col] = True
            
            for dx, dy in direction:
                if dfs(i+1, row+dx, col+dy) is True:
                    return True
                
            visited[row][col] = False
            return False

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == string[0]:
                    if dfs(0, row, col):
                        return True
        return False


matrix = [["a", "b", "c", "e"],
          ["s", "f", "c", "s"],
          ["a", "d", "e", "e"]]
string = "abcbd"
sol = Solution()
print(sol.hasPath(string, matrix))