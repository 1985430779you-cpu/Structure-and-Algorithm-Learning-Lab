class Solution:
    def minimumDeleteSum(self, s1, s2):
        m = len(s1)
        n = len(s2)
        sum1, sum2 = 0, 0
        for i in s1:
            sum1 += ord(i)
        for j in s2:
            sum2 += ord(j)
        f = [[0]*(n+1) for _ in range(m+1)]

        for i, x in enumerate(s1):
            for j, y in enumerate(s2):
                if x == y:
                    f[i+1][j+1] = f[i][j] + ord(x)
                else:
                    f[i+1][j+1] = max(f[i+1][j], f[i][j+1])
        return sum1+sum2-2*f[m][n]

class Solution1:
    def minimumDeleteSum(self, s1, s2):
        m = len(s1)
        n = len(s2)
        f = [[0]*(n+1) for _ in range(m+1)]
        for j in range(n):
            f[0][j+1] = f[0][j]+ord(s2[j])

        for i, x in enumerate(s1):
            f[i+1][0] = f[i][0]+ord(s1[i])
            for j, y in enumerate(s2):
                if x == y:
                    f[i+1][j+1] = f[i][j]
                else:
                    f[i+1][j+1] = min(f[i+1][j] + ord(s2[j]), f[i][j+1] + ord(s1[i]))
        return f[m][n]
    
word1 = "delete"
word2 = "leet"
sol = Solution1()
print(sol.minimumDeleteSum(word1, word2))