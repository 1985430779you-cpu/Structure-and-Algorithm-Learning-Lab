class Solution:
    def maxDotProduct(self, nums1, nums2):
        import math
        m, n = len(nums1), len(nums2)
        from functools import cache
        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return -math.inf
            x = nums1[i] * nums2[j]
            return max(x, x+dfs(i-1,j-1), dfs(i-1, j), dfs(i, j-1))
        return dfs(m-1, n-1)

class Solution:
    def maxDotProduct(self, nums1, nums2):
        import math
        m, n = len(nums1), len(nums2)
        f = [[-math.inf]*(n+1) for _ in range(m+1)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                mult = x * y
                f[i+1][j+1] = max(mult, mult+f[i][j], f[i+1][j], f[i][j+1])
        return f[m][n]
    
nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
sol = Solution()
print(sol.maxDotProduct(nums1, nums2))