class Solution:
    def isMatch(self, string, mode):
        m, n = len(string)+1, len(mode)+1
        boolean_matrix = [[False for _ in range(n)] for _ in range(m)]
        boolean_matrix[0][0] = True

        for j in range(2, n, 2):
            if mode[j-1] == "*":
                boolean_matrix[0][j] = boolean_matrix[0][j-2]

        for i in range(1, m):
            for j in range(1, n):
                if mode[j-1] != "*":
                    if boolean_matrix[i-1][j-1] and string[i-1] == mode[j-1]:
                        boolean_matrix[i][j] = True
                    elif boolean_matrix[i-1][j-1] and mode[j-1] == ".":
                        boolean_matrix[i][j] = True
                elif mode[j-1] == "*":
                    if boolean_matrix[i][j-2]:
                        boolean_matrix[i][j] = True
                    elif boolean_matrix[i-1][j] and string[i-1] == mode[j-2]:
                        boolean_matrix[i][j] = True
                    elif boolean_matrix[i-1][j] and mode[j-2] == ".":
                        boolean_matrix[i][j] = True

        return boolean_matrix[m-1][n-1]

string = "aaa"
ob_string = "ab*.*"
sol = Solution()
print(sol.isMatch(string, ob_string))