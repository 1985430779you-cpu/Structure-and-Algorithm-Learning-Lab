class Solution:
    def searchMatrix(self, matrix, target):
        import numpy as np
        matrix = np.asarray(matrix)
        m, n = matrix.shape

        if matrix[m-1][n-1] < target:
            return False

        low, high = 0, m-1
        while low <= high:
            mid = (low+high) // 2
            if matrix[mid][-1] >= target:
                high = mid-1
            else:
                low = mid+1
        row = low

        low, high = 0, n-1
        while low <= high:
            mid = (low+high) // 2
            if matrix[row][mid] >= target:
                high = mid - 1
            else:
                low = mid+1
        
        col = low
        if matrix[row][col] == target:
            return True
        return False 
