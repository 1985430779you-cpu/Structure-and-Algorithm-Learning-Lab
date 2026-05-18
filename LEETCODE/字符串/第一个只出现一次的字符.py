class Solution:
    def LeftRotateString(self, s, k):
        n = len(s)
        if n == 0 or k <= 0:
            return s
        if n <= k:
            k = k % n
        return s[k:] + s[:k]
    
s = "abcXYZdef"
k = 9
sol = Solution()
print(sol.LeftRotateString(s, k))