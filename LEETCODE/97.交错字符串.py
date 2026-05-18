#重点复习dp：交叉子串
class Solution:
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if m + n != l:
            return False
        from functools import cache
        @cache
        def dfs(i, j):
            if i < 0 and j <0:
                return True
            if (i >= 0 and s1[i] == s3[i+j+1] and dfs(i-1, j)) or (j >= 0 and s2[j] == s3[i+j+1] and dfs(i, j-1)):
                return True
            else:
                return False
        return dfs(m-1, n-1)
    
class Solution1:
    def isInterleave(self, s1, s2, s3):
        m, n, l = len(s1), len(s2), len(s3)
        f = [False]*(n+1)
        f[0] = True
        if m + n != l:
            return False
        for j, y in enumerate(s2):
            f[j + 1] = f[j] and y == s3[j]
        for i, x in enumerate(s1):
            f[0] = f[0] and x == s3[i]
            for j, y in enumerate(s2):
                f[j + 1] = f[j + 1] and x == s3[i + j + 1] or f[j] and y == s3[i + j + 1]
        return f[n]
    
class Solution2:
    def isInterleave(self, s1, s2, s3):
        m, n, l = len(s1), len(s2), len(s3)
        f = [[False]*(n+1) for _ in range(m+1)]
        f[0][0] = True
        if m + n != l:
            return False
        for j, y in enumerate(s2):
            f[0][j+1] = f[0][j] and y == s3[j]
        for i, x in enumerate(s1):
            f[i+1][0] = f[i][0] and x == s3[i]
            for j, y in enumerate(s2):
                f[i+1][j+1] = (f[i][j+1] and x == s3[i + j + 1]) or (f[i+1][j] and y == s3[i + j + 1])
        return f[m][n]
   
s1 = "aabcc" 
s2 = "dbbca"
s3 = "aadbbbaccc"
sol = Solution1()
print(sol.isInterleave(s1, s2, s3))