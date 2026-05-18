class Solution:
    def findTarget(self, array, target):
        rows = len(array)
        cols = len(array[0])

        if rows > 0 and cols > 0:
            row = 0
            col = cols - 1

        while row < rows and col >= 0:
            if array[row][col] == target:
                return True
            elif array[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
    
a = [[1, 2, 8, 9],
     [2, 4, 9, 12],
     [4, 7, 10, 13],
     [6, 8, 11, 15]]
target = 4

sol = Solution()
print(sol.findTarget(a, target))