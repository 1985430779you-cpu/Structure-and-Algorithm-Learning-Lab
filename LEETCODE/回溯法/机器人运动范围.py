class Solution:
    def robotMoving(self, rows, cols, target):
        if rows <= 0 or cols <= 0 or target < 0:
            return 0
        
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        def digitsum(number):
            sum = 0
            while number:
                sum += number % 10
                number //= 10
            return sum
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            if visited[row][col]:
                return 0
            if digitsum(row) + digitsum(col) > target:
                return 0
            
            visited[row][col] = True
            
            total = 1
            for dx, dy in direction:
                total += dfs(row+dx, col+dy)
            return total            

        return dfs(0, 0)

m, n = 3, 3
target = 5
sol = Solution()
print(sol.robotMoving(m, n, target))