class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        f = [[0] * (n+1) for _ in range(m+1)]

        for i, x in enumerate(word1):
            for j, y in enumerate(word2):
                if x == y:
                    f[i+1][j+1] = f[i][j] + 1
                else:
                    f[i+1][j+1] = max(f[i][j+1], f[i+1][j])
        
        return m+n-f[m][n]*2

word1 = "sea"
word2 = "eat"
sol = Solution()
print(sol.minDistance(word1, word2))