class Solution:
    def findPeakGrid(self, mat):
        n = len(mat)
        low, high = 0, n-2
        while low <= high:
            mid = (low+high) // 2
            mx = max(mat[mid])
            if mx > mat[mid+1][mat[mid].index(mx)]:
                high = mid-1
            else:
                low = mid+1

        return [low, mat[low].index(max(mat[low]))]