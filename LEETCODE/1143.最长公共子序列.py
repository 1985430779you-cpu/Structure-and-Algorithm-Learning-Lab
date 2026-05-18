class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m =len(text1)
        n = len(text2)
        from functools import cache
        @cache #减少回溯时间复杂度
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
              
            if text1[i] == text2[j]:
                return dfs(i-1, j-1)+1
            else:
                return max(dfs(i-1, j), dfs(i, j-1))
              
        return dfs(m-1, n-1)