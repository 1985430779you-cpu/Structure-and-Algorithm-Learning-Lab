class Solution:
    def shortestCommonSupersequence(self, str1, str2):
        #1.计算LCS和dp表
        m, n = len(str1), len(str2)
        f = [[0]*(n+1) for _ in range(m+1)]
        for i, x in enumerate(str1):
            for j, y in enumerate(str2):
                if x == y:
                    f[i+1][j+1] = f[i][j] + 1
                else:
                    f[i+1][j+1] = max(f[i+1][j], f[i][j+1])
        #2.从后向前构建SCS
        i, j = m, n
        result = []
        while i >= 1 and j >= 1:
            if str1[i-1] == str2[j-1]:
                result.append(str1[i-1])
                i -= 1
                j -= 1
            elif f[i-1][j] > f[i][j-1]:
                result.append(str1[i-1])
                i -= 1
            else:
                result.append(str2[j-1])
                j -= 1
        #3.处理剩余部分
        while i >= 1:
            result.append(str1[i-1])
            i -= 1
        while j >= 1:
            result.append(str2[j-1])
            j -= 1    
        return "".join(result[::-1]) #从后向前处理：反置
        
str1 = "abac"
str2 = "cab"
sol = Solution()
print(sol.shortestCommonSupersequence(str1, str2))