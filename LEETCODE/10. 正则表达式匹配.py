class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s)+1, len(p)+1
        #创建布尔矩阵
        boolean_matrix = []
        for _ in range(0, m):
            matrix = [False]*n
            boolean_matrix.append(matrix)
        boolean_matrix[0][0] = True
        #第一行空字符匹配
        for j in range(2, n, 2):
            boolean_matrix[0][j] == boolean_matrix[0][j-2] and p[j-1] == "*"
        #布尔矩阵运算，最后一个输出为真即代表匹配
        for i in range(1, m):
            for j in range(1, n):
                if p[j-1] != "*":
                    if boolean_matrix[i-1][j-1] and s[i-1] == p[j-1]:
                        boolean_matrix[i][j] = True
                    elif boolean_matrix[i-1][j-1] and p[j-1] == ".":
                        boolean_matrix[i][j] = True
                elif p[j-1] == "*":
                    if boolean_matrix[i][j-2]:
                        boolean_matrix[i][j] = True
                    elif boolean_matrix[i-1][j] and s[i-1] == p[j-2]:
                        boolean_matrix[i][j] = True
                    elif boolean_matrix[i-1][j] and p[j-2] == ".":
                        boolean_matrix[i][j] = True
        return boolean_matrix[m-1][n-1]
    
string = "aaa"
ob_string = "ab*.*"
sol = Solution()
print(sol.isMatch(string, ob_string))