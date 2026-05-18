class Solution:
    def longestSemiRepetitiveSubstring(self, s):
        n = len(s)
        if n <= 0:
            return 0
        
        pos = 0
        i = 0
        ans = 0
        count = 0
        for j in range(n):
            if j > 0 and s[j] == s[j-1]:
                count += 1
                if count > 1:
                    i = pos
                    count -= 1
                pos = j
            ans = max(ans, j-i+1)
        return ans
    
s = "1111111"
sol = Solution()
print(sol.longestSemiRepetitiveSubstring(s))