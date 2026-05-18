class Solution:
    def printMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        top, bottom, left, right = 0, rows-1, 0, cols-1
        ans = []

        while top < bottom or left < right:
            for i in range(left, right):
                ans.append(matrix[top][i])
            for i in range(top, bottom):
                ans.append(matrix[i][right])
            for i in range(right, left, -1):
                ans.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                ans.append(matrix[i][left])

            top += 1
            left += 1
            bottom -= 1
            right -= 1

        return ans

m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
sol = Solution()
print(sol.printMatrix(m))